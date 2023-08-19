#!/usr/bin/python3
"""defining unittest for amenity identification"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """defining test cases for amenity"""

    def test_amenity_instance(self):
        """defining amenity instances"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIs(type(amenity), Amenity)

    def test_amenity_attributes(self):
        """defining amenity attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_inherits_from_base_model(self):
        """inheriting amenity from base model"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_amenity_to_dict(self):
        """testing amenity from dict"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertTrue('id' in amenity_dict)
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)
        self.assertTrue('name' in amenity_dict)

    def test_amenity_to_str(self):
        """testing amenity to string representations"""
        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertTrue('[Amenity]' in amenity_str)
        self.assertTrue('id' in amenity_str)
        self.assertTrue('created_at' in amenity_str)
        self.assertTrue('updated_at' in amenity_str)
        self.assertTrue('name' in amenity_str)


if __name__ == '__main__':
    unittest.main()
