#!/usr/bin/python3
"""A module that stores State inherited from BaseModel"""


from models.base_model import BaseModel
from datetime import datetime


class State(BaseModel):
    """A class that stores State information for BaseModel"""

    name = ""
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
        State.count += 1

    def __del__(self):
        State.count -= 1
