import json
from models import Fruta

DATA_FILE = "fruits.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def create_fruit(fruit: Fruta):
    data = load_data()
    new_id = max([item['id'] for item in data], default=0) + 1
    fruit_dict = fruit.to_dict()
    fruit_dict['id'] = new_id
    data.append(fruit_dict)
    save_data(data)

def read_fruits():
    return load_data()

def update_fruit(fruit_id: int, updated_fruit: Fruta):
    data = load_data()
    for item in data:
        if item['id'] == fruit_id:
            item.update(updated_fruit.to_dict())
            save_data(data)
            return
    raise ValueError("Fruit not found")

def delete_fruit(fruit_id: int):
    data = load_data()
    data = [item for item in data if item['id'] != fruit_id]
    save_data(data)
