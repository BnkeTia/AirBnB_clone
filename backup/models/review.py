#!/usr/bin/python3
"""Definition of a class to reveiew the process"""

from models.base_model import BaseModel


class Review(BaseModel):
    """creating pbject instances for thr class Review"""
    place_id = ""
    user_id = ""
    text = ""
