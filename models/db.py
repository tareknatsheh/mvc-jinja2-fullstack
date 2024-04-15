import json

def get_data():
    with open("./models/data.json") as f:
        data = json.load(f)
        return data