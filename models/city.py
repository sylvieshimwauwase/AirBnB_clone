#!/usr/bin/python3
"""defining city class inheriting from base model"""

from models.base_model import BaseModel


class City(BaseModel):
    """representing city class"""

    def __init__(self, *args, **kwargs):
        """defining city attributes"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
