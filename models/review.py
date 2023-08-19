#!/usr/bin/python3
"""This is an AirBnB Python package having the Review class defined"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A review class that inherits from BaseModel

    Keyword arguments:
    argument -- void
    Return: void
    """

    place_id = ""
    user_id = ""
    text = ""
