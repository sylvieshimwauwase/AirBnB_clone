#!/usr/bin/python3
"""This module contains a File Storage class for the AirBnB"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    __modelClasses = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        """This method returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """
        This method setts in __objects the give
        obj with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """This method serializes __objects to a JSON file"""
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """This method deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as f:
                new_objects = json.load(f)
            self.__objects = {
                key: self.__modelClasses[val.get("__class__")](**val)
                for key, val in new_objects.items()
            }
