import os
import json

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def is_file_empty(file_path):
    with open(file_path, 'r') as file:
        return not file.read().strip()

def get_directory_contents(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_file_size(file_path):
    return os.path.getsize(file_path)

def create_directory(directory):
    os.makedirs(directory, exist_ok=True)