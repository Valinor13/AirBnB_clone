#!/usr/bin/python3
"""A module that stores Review inherited from BaseModel"""


from models.base_model import BaseModel
from datetime import datetime


class Review(BaseModel):
    """A class that stores reviews of HBnB listings"""

    place_id = ""
    user_id = ""
    text = ""
    count = 0

    def __init__(self, *args, **kwargs):
        if not kwargs or len(kwargs) == 0:
            super().__init__()
        else:
            time_fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for k in kwargs:
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    kwargs[k] = datetime.strptime(kwargs[k], time_fmt)
                setattr(self, k, kwargs[k])
        Review.count += 1

    def __del__(self):
        Review.count -= 1
