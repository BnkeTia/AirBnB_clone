#!/usr/bin/python3
"""Importing needed modules from standard python lib"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Definition of a superclass called BaseModel"""
    def __init__(self):
        """assigning a uuid when an instance is created"""
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now()

    def __str__(self):
        """setting str to return key values"""
        return "{}".format(self.__dict__)

    def save(self):
        """updates the updated_at attribute with currebt tine"""
        self.updated_at = datetime.now()
# print(BaseModel().id) either this or the code below


bm_1 = BaseModel()
print(bm_1.id)
print(bm_1.created_at)  # print the datetime in iso format
print(type(bm_1.created_at))  # print the type of datetime
