#!/usr/bin/python3
"""defining amenity class inheriting from base model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """representing amenity class"""
    def __init__(self, *args, **kwargs):
        """defining amenity attributes"""
        super().__init__(*args, **kwargs)
        self.name = ""
