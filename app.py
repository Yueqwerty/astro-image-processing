from flask import Flask, request, jsonify, render_template
from utils.image_processing import process_astronomical_image
from utils.persistence import load_data, save_data, get_data_by_id, update_data_by_id, delete_data_by_id
import os
import uuid

app = Flask(__name__)

# Configuración de rutas
DATA_FILE = 'data/data.json'
IMAGE_FOLDER = 'data/images'
PROCESSED_IMAGE_FOLDER = 'data/processed_images'
os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_IMAGE_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        # Guardar imagen
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        filepath = os.path.join(IMAGE_FOLDER, filename)
        file.save(filepath)
        
        # Procesar imagen
        result = process_astronomical_image(filepath)
        
        # Guardar resultados en persistencia
        data = load_data(DATA_FILE)
        new_entry = {
            'id': len(data),
            'filename': filename,
            'result': result
        }
        data.append(new_entry)
        save_data(DATA_FILE, data)
        
        return jsonify(new_entry), 200

@app.route('/data', methods=['GET'])
def get_data():
    data = load_data(DATA_FILE)
    return jsonify(data), 200

@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id_route(id):
    entry = get_data_by_id(DATA_FILE, id)
    if entry:
        return jsonify(entry), 200
    return jsonify({'error': 'Data not found'}), 404

@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.json
    data = load_data(DATA_FILE)
    new_data['id'] = len(data)
    data.append(new_data)
    save_data(DATA_FILE, data)
    return jsonify(new_data), 201

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    updated_data = request.json
    updated_entry = update_data_by_id(DATA_FILE, id, updated_data)
    if updated_entry:
        return jsonify(updated_entry), 200
    return jsonify({'error': 'Data not found'}), 404

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    deleted_entry = delete_data_by_id(DATA_FILE, id)
    if deleted_entry:
        return jsonify(deleted_entry), 200
    return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
