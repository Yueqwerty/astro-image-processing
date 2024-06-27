import os
import uuid
from flask import Flask, request, jsonify, send_from_directory, Response
from astro_utils.image_processing import process_astronomical_image, classify_galaxy
from flask_cors import CORS
from pymongo import MongoClient
import gridfs

app = Flask(__name__)
CORS(app)

# Configuración de MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['galaxy_classification_db']
fs = gridfs.GridFS(db)
images_collection = db['images']

# Rutas de carpetas
IMAGE_FOLDER = 'data/images'
PROCESSED_IMAGE_FOLDER = 'data/processed_images'
TRAINING_IMAGES_FOLDER = 'data/training_images'
CLASSIFICATIONS = ['Espiral', 'Eliptica', 'Irregular']

for classification in CLASSIFICATIONS:
    os.makedirs(os.path.join(TRAINING_IMAGES_FOLDER, classification), exist_ok=True)

os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_IMAGE_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "Welcome to the Galaxy Classification API"

@app.route('/process_images', methods=['POST'])
def process_images():
    if 'files' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    files = request.files.getlist('files')
    if not files:
        return jsonify({'error': 'No selected files'}), 400
    
    responses = []
    
    for file in files:
        filename = f"{uuid.uuid4()}.jpg"
        file_path = os.path.join(IMAGE_FOLDER, filename)
        file.save(file_path)
        
        result = process_astronomical_image(file_path)
        classification = classify_galaxy(result['processed'])
        
        # Mover la imagen procesada a la carpeta correspondiente
        training_image_path = os.path.join(TRAINING_IMAGES_FOLDER, classification, os.path.basename(result['processed']))
        os.rename(result['processed'], training_image_path)
        
        # Guardar la imagen procesada en MongoDB
        with open(training_image_path, 'rb') as img_file:
            processed_file_id = fs.put(img_file, filename=f"processed_{filename}")
        
        images_collection.insert_one({
            'filename': filename,
            'processed_image_filename': os.path.basename(training_image_path),
            'classification': classification
        })
        
        responses.append({
            'filename': filename,
            'processed_image_filename': os.path.basename(training_image_path),
            'classification': classification
        })
    
    return jsonify(responses), 200

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/processed/<filename>')
def send_processed_file(filename):
    file_data = images_collection.find_one({'processed_image_filename': filename})
    if not file_data:
        return jsonify({'error': 'File not found'}), 404
    file = fs.get_last_version(filename=f"processed_{file_data['filename']}")
    return Response(file.read(), content_type='image/jpeg')

@app.route('/data', methods=['GET'])
def get_data():
    images = list(images_collection.find({}, {'_id': 0}))
    return jsonify(images), 200

@app.route('/data/<string:filename>', methods=['DELETE'])
def delete_data(filename):
    image_data = images_collection.find_one({'filename': filename})
    if not image_data:
        return jsonify({'error': 'File not found'}), 404
    
    file_id = fs.get_last_version(filename=f"processed_{image_data['filename']}")._id
    fs.delete(file_id)
    
    images_collection.delete_one({'filename': filename})
    
    return jsonify({'message': 'Data deleted successfully'}), 200

@app.route('/report', methods=['GET'])
def generate_report():
    images = list(images_collection.find({}, {'_id': 0}))
    report = {
        'total_images': len(images),
        'classifications': {
            'Espiral': len([img for img in images if img['classification'] == 'Espiral']),
            'Elíptica': len([img for img in images if img['classification'] == 'Elíptica']),
            'Irregular': len([img for img in images if img['classification'] == 'Irregular'])
        }
    }
    return jsonify(report), 200

@app.route('/statistics', methods=['GET'])
def get_statistics():
    total_images = images_collection.count_documents({})
    classifications = images_collection.aggregate([
        {"$group": {"_id": "$classification", "count": {"$sum": 1}}}
    ])
    
    stats = {
        "total_images": total_images,
        "classifications": {doc['_id']: doc['count'] for doc in classifications}
    }
    
    return jsonify(stats), 200

@app.route('/image/<string:filename>', methods=['GET'])
def get_image_details(filename):
    image_data = images_collection.find_one({'filename': filename}, {'_id': 0})
    if not image_data:
        return jsonify({'error': 'File not found'}), 404
    return jsonify(image_data), 200

if __name__ == '__main__':
    app.run(debug=True)
