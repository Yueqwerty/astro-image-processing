import json
import os

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def get_data_by_id(file_path, id):
    data = load_data(file_path)
    for entry in data:
        if entry['id'] == id:
            return entry
    return None

def update_data_by_id(file_path, id, updated_data):
    data = load_data(file_path)
    for i, entry in data:
        if entry['id'] == id:
            data[i] = updated_data
            save_data(file_path, data)
            return updated_data
    return None

def delete_data_by_id(file_path, id):
    data = load_data(file_path)
    for i, entry in data:
        if entry['id'] == id:
            deleted_entry = data.pop(i)
            save_data(file_path, data)
            return deleted_entry
    return None
