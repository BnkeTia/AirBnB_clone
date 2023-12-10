#!/usr/bin/python3
import uuid
from datetime import datetime

# Creating an alias to avoid flake errors
datstrpt = datetime.strptime


class BaseModel:
    """superclass called BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel attributes"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "update_at":
                    self.__dict__["ipdate_at"] = datetime.strptime(
                            kwags["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[i] = kwargs[i]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel"""
        return ("[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__))

    def save(self):
        """Update updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = new_dict["created_at"].isoformat()
        new_dict['updated_at'] = new_dict["updated_at"].isoformat()
        return (new_dict)
