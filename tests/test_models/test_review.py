#!/usr/bin/python3
"""A module for unittests for the user class"""



import unittest
import os
from models.review import Review
from models.engine.file_storage import FileStorage


fs = FileStorage()


class TestUser(unittest.TestCase):
    """class to test Review"""

    def test_place_id(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Review()
        self.assertIsInstance(u1.place_id, str)

    def test_user_id(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Review()
        self.assertIsInstance(u1.user_id, str)

    def test_text(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = Review()
        u1.text = "blah"
        self.assertIsInstance(u1.text, str)

    if __name__ == '__main__':
        unittest.main()
