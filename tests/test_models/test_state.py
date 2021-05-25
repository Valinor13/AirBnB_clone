#!/usr/bin/python3
"""A module for unittests for the user class"""



import unittest
import os
from models.state import State
from models.engine.file_storage import FileStorage


fs = FileStorage()


class TestUser(unittest.TestCase):
    """class to test State"""

    def test_name(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        u1 = State()
        self.assertIsInstance(u1.name, str)

    if __name__ == '__main__':
        unittest.main()
