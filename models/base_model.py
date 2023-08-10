#!/usr/bin/python3
"""This is an AirBnB Python package having the Base Model class defined"""
import uuid
from datetime import datetime
# from models import storage


class BaseModel:
    """The AirBnB Base Model class"""

    def __init__(self, *args, **kwargs):
        """The Base Model class constructor"""
        if kwargs.items():
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)

    def __str__(self):
        """The string representation of the Base Model class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method saves the object attributes to the storage"""
        self.updated_at = datetime.now()
        # storage.save()

    def to_dict(self):
        """This method convert the object attributes to a dictionary"""
        my_dict = {key: value for key, value in self.__dict__.items()}
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
