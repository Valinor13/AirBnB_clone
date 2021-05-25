#!/usr/bin/python3
"""A module for unittests for the user class"""



import unittest
import os
from models.city import City
from models.engine.file_storage import FileStorage


fs = FileStorage()
u1 = City()


class TestUser(unittest.TestCase):
    """class to test City"""

    def test_state_id(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = City()
        self.assertIsInstance(u1.state_id, str)

    def test_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = City()
        self.assertIsInstance(u1.name, str)

    if __name__ == '__main__':
        unittest.main()
