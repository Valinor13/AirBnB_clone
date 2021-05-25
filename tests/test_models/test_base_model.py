#!/usr/bin/python3
"""A module for unittests for the base model class"""


import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


fs = FileStorage()


class TestBaseModel(unittest.TestCase):
    """A class to test BaseModel"""

    def test_filestorage_reload(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        dic = fs._FileStorage__objects
        bm1.my_number = 89
        self.assertEqual(bm1.my_number, 89)
        fs.reload()
        self.assertEqual(dic, fs._FileStorage__objects)

    def test_filestorage_save(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        self.assertNotEqual(os.path.getsize(fs._FileStorage__file_path), 0)

    def test_filestorage_new(self):
        bm1 = BaseModel()
        self.assertNotEqual(len(fs._FileStorage__objects), 0)

    def test_filestorage_all(self):
        bm1 = BaseModel()
        self.assertIsInstance(fs.all(), dict)

    def test_filestorage_objects(self):
        bm1 = BaseModel()
        self.assertIsInstance(fs._FileStorage__objects, dict)

    def test_file_exists(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        bm1 = BaseModel()
        bm1.save()
        self.assertTrue(os.path.exists(fs._FileStorage__file_path))

    def test_id_assignment(self):
        bm1 = BaseModel()
        self.assertNotEqual(bm1.id, "")

    def test_created_at_exists(self):
        bm1 = BaseModel()
        self.assertIsInstance(type(bm1.created_at), type(datetime))

    def test_updated_at_exists(self):
        bm1 = BaseModel()
        self.assertIsInstance(type(bm1.updated_at), type(datetime))

    def test_str_output(self):
        bm1 = BaseModel()
        self.assertIn("BaseModel", bm1.__str__())
        self.assertIn(str(bm1.id), bm1.__str__())
        self.assertIn(str(bm1.__dict__), bm1.__str__())

    def test_save_method(self):
        bm1 = BaseModel()
        original = bm1.updated_at
        bm1.save()
        new = bm1.updated_at
        self.assertNotEqual(original, new)

    def test_to_dict_method(self):
        bm1 = BaseModel()
        my_dict = bm1.to_dict()
        self.assertIn("__class__", my_dict.keys())

    def test_init_kwargs(self):
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        bm2 = BaseModel(**bm1_dict)
        self.assertEqual(type(bm2), type(bm1))
        self.assertIsNot(bm2, bm1)
        self.assertEqual(bm2.id, bm1.id)
        self.assertEqual(bm2.created_at, bm1.created_at)

    if __name__ == '__main__':
        unittest.main()
