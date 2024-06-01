#!/usr/bin/python3
"""Defines a module"""
import json, os


class FileStorage:
    """Defines a class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            obj_dict = {key: obj.todict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    cls = eval(class_name)
                    self.__objects[key] = cls(**value)
