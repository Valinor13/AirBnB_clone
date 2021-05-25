#!/usr/bin/python3
"""A module that stores Place inherited from BaseModel"""


from models.base_model import BaseModel
from datetime import datetime


class Place(BaseModel):
    """A class that stores place profile of HBnB listings"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
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
        Place.count += 1

    def __del__(self):
        Place.count -= 1
