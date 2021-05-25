#!/usr/bin/python3
"""A module for unittests for the file storage class"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A class to test FileStorage"""

    def test_filestorage_reload(self):
        fs = FileStorage()
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        fs.reload()
        dic = fs._FileStorage__objects.copy()
        bm1.my_number = 89
        self.assertEqual(bm1.my_number, 89)
        fs.reload()
        self.assertNotEqual(dic, fs._FileStorage__objects)

    def test_filestorage_save(self):
        fs = FileStorage()
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        self.assertNotEqual(os.path.getsize(fs._FileStorage__file_path), 0)

    def test_filestorage_new(self):
        fs = FileStorage()
        fs_all = fs.all().copy()
        bm1 = BaseModel()
        self.assertNotEqual(fs.all(), fs_all)

    def test_filestorage_all(self):
        fs = FileStorage()
        bm1 = BaseModel()
        self.assertIsInstance(fs.all(), dict)

    def test_filestorage_objects(self):
        fs = FileStorage()
        bm1 = BaseModel()
        self.assertIsInstance(fs._FileStorage__objects, dict)

    def test_file_exists(self):
        fs = FileStorage()
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        self.assertTrue(os.path.exists(fs._FileStorage__file_path))

if __name__ == '__main__':
    unittest.main()
