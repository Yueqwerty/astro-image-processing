import os
import uuid
from flask import Flask, request, jsonify, render_template, send_from_directory
import cv2
from astro_utils.image_processing import process_astronomical_image, classify_galaxy
import json

app = Flask(__name__)

DATA_FILE = 'data/data.json'
IMAGE_FOLDER = 'data/images'
PROCESSED_IMAGE_FOLDER = 'data/processed_images'
os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_IMAGE_FOLDER, exist_ok=True)

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
    return []

def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processed_images', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = f"{uuid.uuid4()}.jpg"
        filepath = os.path.join(IMAGE_FOLDER, filename)
        file.save(filepath)
        
        result = process_astronomical_image(filepath)
        classification = classify_galaxy(filepath)
        data = load_data(DATA_FILE)
        new_entry = {
            'id': len(data),
            'filename': filename,
            'result': {
                'processed': result['processed'],
                'classification': classification
            }
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
    data = load_data(DATA_FILE)
    entry = next((item for item in data if item['id'] == id), None)
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
    data = load_data(DATA_FILE)
    entry = next((item for item in data if item['id'] == id), None)
    if entry:
        entry.update(updated_data)
        save_data(DATA_FILE, data)
        return jsonify(entry), 200
    return jsonify({'error': 'Data not found'}), 404

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    data = load_data(DATA_FILE)
    entry = next((item for item in data if item['id'] == id), None)
    if entry:
        data.remove(entry)
        save_data(DATA_FILE, data)
        return jsonify(entry), 200
    return jsonify({'error': 'Data not found'}), 404

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/processed/<filename>')
def send_processed_file(filename):
    return send_from_directory(PROCESSED_IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
