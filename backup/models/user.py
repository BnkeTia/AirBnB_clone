#!/usr/bin/python3
"""Definition of the class user"""

from models.base_model import BaseModel

class User(BaseModel):
    """creating instances for the user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
