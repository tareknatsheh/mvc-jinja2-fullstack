import json

def validate_data(fn):
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        if not isinstance(data, dict):
            raise ValueError("DB structure should be a dictionay")
        
        if len(data.keys()) == 0:
            raise ValueError("DB dict should not be empty")
        
        return data
    
    return wrapper

@validate_data
def get_data(file_path: str):
    with open(file_path) as f:
        data = json.load(f)
        return data