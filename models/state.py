#!/usr/bin/python3
"""inheriting state class from base model"""

from models.base_model import BaseModel


class State(BaseModel):
    """representation of state class"""

    def __init__(self, *args, **kwargs):
        """defining state attributes"""
        super().__init__(*args, **kwargs)
        self.name = ""
