import json

def get_data(file_path: str):
    with open(file_path) as f:
        data = json.load(f)
        return data