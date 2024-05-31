from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import json
import os

app = Flask(__name__)

# Directorio para guardar datos de persistencia dummy
DATA_FILE = 'data.json'

# Cargar datos desde el archivo JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Guardar datos en el archivo JSON
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

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
        # Leer la imagen
        np_img = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        
        # Procesamiento de la imagen (ejemplo simple: convertir a gris)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Guardar resultados en la persistencia dummy
        data = load_data()
        data.append({
            'filename': file.filename,
            'result': 'Processed'
        })
        save_data(data)
        
        return jsonify({'message': 'Image processed', 'result': 'Processed'}), 200

@app.route('/data', methods=['GET'])
def get_data():
    data = load_data()
    return jsonify(data), 200

@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.json
    data = load_data()
    data.append(new_data)
    save_data(data)
    return jsonify(new_data), 201

@app.route('/data/<int:index>', methods=['PUT'])
def update_data(index):
    updated_data = request.json
    data = load_data()
    if 0 <= index < len(data):
        data[index] = updated_data
        save_data(data)
        return jsonify(updated_data), 200
    return jsonify({'error': 'Index out of range'}), 404

@app.route('/data/<int:index>', methods=['DELETE'])
def delete_data(index):
    data = load_data()
    if 0 <= index < len(data):
        deleted_data = data.pop(index)
        save_data(data)
        return jsonify(deleted_data), 200
    return jsonify({'error': 'Index out of range'}), 404

if __name__ == '__main__':
    app.run(debug=True)
