#!/usr/bin/python3
"""
This is the class BaseModel which defines all attributes
for the classes in AirBnb project
"""

from datetime import datetime
import uuid
import models


class BaseModel():

    """defines all attributes and methods of clases"""

    count = 0
    created_at = ""
    updated_at = ""
    id = ""

    def __init__(self, *args, **kwargs):
        if not kwargs or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            time_fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for k in kwargs:
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    kwargs[k] = datetime.strptime(kwargs[k], time_fmt)
                setattr(self, k, kwargs[k])
        BaseModel.count += 1

    def save(self):
        """updates instance attribute update_at"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns dictionary of instance attributes"""
        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic

    def __del__(self):
        """Decrements count on instance deletion"""
        BaseModel.count -= 1

    def __str__(self):
        """returns printable string of object"""
        st = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return st
