#!/usr/bin/python3
"""defining unittest for place identification"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """defining test cases for place"""

    def test_place_instance(self):
        """defining place instances"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIs(type(place), Place)

    def test_place_attributes(self):
        """defining place attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.descrption, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_inherits_from_base_model(self):
        """inheriting place from base model"""
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_place_to_dict(self):
        """testing place from dict"""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertTrue('id' in place_dict)
        self.assertTrue('created_at' in place_dict)
        self.assertTrue('updated_at' in place_dict)
        self.assertTrue('city_id' in place_dict)
        self.assertTrue('user_id' in place_dict)
        self.assertTrue('name' in place_dict)
        self.assertTrue('description' in place_dict)
        self.assertTrue('number_rooms' in place_dict)
        self.assertTrue('number_bathrooms' in place_dict)
        self.assertTrue('max_guest' in place_dict)
        self.assertTrue('price_by_night' in place_dict)
        self.assertTrue('latitude' in place_dict)
        self.assertTrue('longitude' in place_dict)
        self.assertTrue('amenity_ids' in place_dict)

    def test_place_to_str(self):
        """testing place to string representations"""
        place = Place()
        place_str = str(place)
        self.assertTrue('[Place]' in place_str)
        self.assertTrue('id' in place_str)
        self.assertTrue('created_at' in place_str)
        self.assertTrue('updated_at' in place_str)
        self.assertTrue('city_id' in place_str)
        self.assertTrue('user_id' in place_str)
        self.assertTrue('name' in place_str)
        self.assertTrue('description' in place_str)
        self.assertTrue('number_rooms' in place_str)
        self.assertTrue('number_bathrooms' in place_str)
        self.assertTrue('max_guest' in place_str)
        self.assertTrue('price_by_night' in place_str)
        self.assertTrue('latitude' in place_str)
        self.assertTrue('longitude' in place_str)
        self.assertTrue('amenity_ids' in place_str)


if __name__ = '__main__':
    unittest.main()
