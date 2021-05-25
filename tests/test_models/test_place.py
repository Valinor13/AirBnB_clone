#!/usr/bin/python3
"""A module for unittests for the user class"""



import unittest
import os
from models.place import Place
from models.engine.file_storage import FileStorage


fs = FileStorage()


class TestUser(unittest.TestCase):
    """class to test Place"""

    def test_city_id(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        self.assertIsInstance(u1.city_id, str)

    def test_user_id(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        self.assertIsInstance(u1.user_id, str)

    def test_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        u1.name = "blah"
        self.assertIsInstance(u1.name, str)

    def test_description(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        u1.description = "blah"
        self.assertIsInstance(u1.description, str)

    def test_number_rooms(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        u1.number_rooms = 3
        self.assertIsInstance(u1.number_rooms, int)

    def test_number_bathrooms(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        u1.number_bathrooms = 3
        self.assertIsInstance(u1.number_bathrooms, int)

    def test_max_guest(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        u1.max_guest = 4
        self.assertIsInstance(u1.max_guest, int)

    def test_price_by_night(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        u1.price_by_night = 5
        self.assertIsInstance(u1.price_by_night, int)

    def test_latitude(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        u1.latitude = 4.333
        self.assertIsInstance(u1.latitude, float)

    def test_lobgitude(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        u1.longitude = 4.33
        self.assertIsInstance(u1.longitude, float)

    def test_amenity_ids(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Place()
        self.assertIsInstance(u1.amenity_ids, list)

    if __name__ == '__main__':
        unittest.main()
