#!/usr/bin/python3
"""A module for unittests for the user class"""


import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage


fs = FileStorage()


class TestUser(unittest.TestCase):

    """class to test User"""

    u1 = User()

    def test_email(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        self.assertIsInstance(self.u1.email, str)

    def test_password(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        self.assertIsInstance(self.u1.password, str)

    def test_first_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        self.assertIsInstance(self.u1.first_name, str)

    def test_last_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        self.assertIsInstance(self.u1.last_name, str)

if __name__ == '__main__':
    unittest.main()
