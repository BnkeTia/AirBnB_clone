#!/usr/bin/python3
<<<<<<< HEAD
"""Initializer that passes storage function from engine"""

from models.engine.file_storage import FileStorage


=======
"""Initializes package"""
from models.engine.file_storage import FileStorage
>>>>>>> 4fb33810694db6ee7466193faf1616a48a549462
storage = FileStorage()
storage.reload()
