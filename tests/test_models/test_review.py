#!/usr/bin/python3
"""defining unittest for review identification"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """defining test cases for review"""

    def test_review_instance(self):
        """defining review instances"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIs(type(review), Review)

    def test_review_attributes(self):
        """defining review attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_inherits_from_base_model(self):
        """inheriting review from base model"""
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_review_to_dict(self):
        """testing review from dict"""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertTrue('id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)
        self.assertTrue('place_id' in review_dict)
        self.assertTrue('user_id' in review_dict)
        self.assertTrue('text' in review_dict)

    def test_review_to_str(self):
        """testing review to string representations"""
        review = Review()
        review_str = str(review)
        self.assertTrue('[Review]' in review_str)
        self.assertTrue('id' in review_str)
        self.assertTrue('created_at' in review_str)
        self.assertTrue('updated_at' in review_str)
        self.assertTrue('place_id' in review_str)
        self.assertTrue('user_id' in review_str)
        self.assertTrue('text' in review_str)


if __name__ == '__main__':
    unittest.main()
