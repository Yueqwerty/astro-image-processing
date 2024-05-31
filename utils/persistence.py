import json
import os

def load_data(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return []
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
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
    for i, entry in enumerate(data):
        if entry['id'] == id:
            data[i] = updated_data
            save_data(file_path, data)
            return updated_data
    return None

def delete_data_by_id(file_path, id):
    data = load_data(file_path)
    for i, entry in enumerate(data):
        if entry['id'] == id:
            deleted_entry = data.pop(i)
            save_data(file_path, data)
            return deleted_entry
    return None
