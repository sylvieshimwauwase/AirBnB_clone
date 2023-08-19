#!/usr/bin/python3
"""This is an AirBnB Python package having the City class defined"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A city class that inherits from BaseModel

    Keyword arguments:
    argument -- void
    Return: void
    """

    state_id = ""
    name = ""
