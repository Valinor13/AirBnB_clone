#!/usr/bin/python3
"""Serializes and deserializes json files"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """serializes and deserializes json file"""
    __file_path = "HBNB_Listings.json"
    __objects = dict()

    def all(self):
        """returns dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        obj2 = obj.to_dict()
        obj_key = str(obj2["__class__"])
        obj_key = obj_key + "." + obj2["id"]
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes object to the json file"""
        dic = dict()
        with open(FileStorage.__file_path, 'w') as fh:
            for k in FileStorage.__objects:
                dic[k] = FileStorage.__objects[k].to_dict()
            json.dump(dic, fh)

    def reload(self):
        """deserializes json file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fh:
                obj_dic = json.load(fh)
            for k in obj_dic:
                FileStorage.__objects[k] = obj_dic[k]
            for k in FileStorage.__objects:
                key_list = k.split(".")
                cls = key_list[0]
                inst = eval(cls)
                FileStorage.__objects[k] = inst(
                    **dict(FileStorage.__objects[k]))
