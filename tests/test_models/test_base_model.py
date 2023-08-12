#!/usr/bin/python3
"""unittest for base_model.py"""

import unittest
from models.base_model import BaseModel
import sys


class TestBaseModel(unittest.TestCase):
    """class to test BaseModel"""

    def test_init_with_kwargs(self):
        """test initialization with kwargs"""
        base_model = BaseModel(
                id='123',
                created_at='2023-08-01T12:00:00',
                updated_at='2023-08-01T13:00:00'
                )
        self.assertEqual(base_model.id, '123')
        self.assertEqual(
                base_mode.created_at.isoformat(),
                '2023-08-01T12:00:00'
                )
        self.assertEqual(
                base_model.updated_at.isoformat(),
                '2023-08-01T13:00:00'
                )

    def test_str(self):
        """test str"""
        str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), str)

    def test_save(self):
        """test updates on updated_at instance"""
        updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, updated_at)

    def test_to_dict(self):
        """test conversion of instance attributes to a dictionary"""
        dict = {
                'id': self.base_model.id,
                'created_at': self.base_model.created_at.isoformat(),
                'updated_at': slef.base_model.updated_at.isoformat(),
                '__class__': 'BaseModel'
                }
        self.assertEqual(base_model.to_dict(), dict)


if __name__ == '__main__':
    unittest.main()
