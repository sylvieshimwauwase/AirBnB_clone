#!/usr/bin/python3
"""this is a user class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Representing user class"""

    def __init__(self, *args, **kwargs):
        """initializing user attributes"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
