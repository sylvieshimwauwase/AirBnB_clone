#!/usr/bin/python3
"""adding unittest cases for file storage"""

import unittest
import os
import models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """unittest for file storage"""

    def setUp(self):
        """ensuring a clean env on each test"""
        storage.reload()
        self.file_path = "test_file.json"

    def tearDown(self):
        """generating clean up after each test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_empty(self):
        """testing if all methods returns empty dictionary"""
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 0)

    def test_new_all(self):
        """testing adding new objects"""
        model = BaseModel()
        storage.new(model)
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 1)
        self.assertIn(model, objects.values())

    def test_save_reload(self):
        """test saving and reload objects"""
        model = BaseModel()
        storage.new(model)
        storage.save()

        new_storage = storage.__class__()
        new_storage.reload()
        objects = new_storage.all()

        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 1)
        self.assertIn(model, objects.values())

    def test_nonexist_file(self):
        """test if file does not exist"""
        non_existent_storage = storage.__class__()
        non_existent_storage.reload()
        objects = non_existent_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 0)

    def test_reload_invalid(self):
        """test reload if it is an invalid file"""
        with open(self.file_path, "w") as f:
            f.write("invalid json data")
        invalid_storage = storage.__class__()
        invalid_storage.reload()
        objects = invalid_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 0)

    def test_reload_class(self):
        """test if reload with valid data but incorrect class"""
        data = {"BaseModel.123": {
            "__class__": "NonExistentClass", "id": "123"}
            }
        with open(self.file_path, "w") as f:
            json.dump(data, f)
        invalid_class_storage = storage.__class__()
        invalid_class_storage.reload()
        objects = invalid_class_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 0)


if __name__ == '__main__':
    unittest.main()
