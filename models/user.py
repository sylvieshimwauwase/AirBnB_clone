#!/usr/bin/python3
"""This is an AirBnB Python package having the User class defined"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A user class that inherits from BaseModel

    Keyword arguments:
    argument -- void
    Return: void
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
