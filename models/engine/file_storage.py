# models/engine/file_storage.py
import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file & deserializes JSON file to instances."""
    
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds obj to __objects with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj_id, obj_data in obj_dict.items():
                    cls_name = obj_data['__class__']
                    if cls_name == 'BaseModel':
                        self.__objects[obj_id] = BaseModel(**obj_data)
        except FileNotFoundError:
            pass

