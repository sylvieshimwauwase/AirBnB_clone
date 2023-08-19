#!/usr/bin/python3
"""unittests for city class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """defining test cases for city"""

    def test_city_instance(self):
        """defining city instances"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIs(type(city), City)

    def test_city_attributes(self):
        """defining city attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_inherits_from_base_model(self):
        """inheriting city from base model"""
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_city_to_dict(self):
        """testing city from dict"""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertTrue('id' in city_dict)
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)
        self.assertTrue('state_id' in city_dict)
        self.assertTrue('name' in city_dict)

    def test_city_to_str(self):
        """testing city to string representations"""
        city = City()
        city_str = str(city)
        self.assertTrue('[City]' in city_str)
        self.assertTrue('id' in city_str)
        self.assertTrue('created_at' in city_str)
        self.assertTrue('updated_at' in city_str)
        self.assertTrue('state_id' in city_str)
        self.assertTrue('name' in city_str)


if __name__ == '__main__':
    unittest.main()
