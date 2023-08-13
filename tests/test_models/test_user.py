#!/usr/bin/python3
"""this is the unittest case for user"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test cases for users"""

    def test_user_instance(self):
        """testing the instances of user"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIs(type(user), User)

    def test_user_attributes(self):
        """testing the attributes of a user"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_inherits_from_base_model(self):
        """testing the inheritance of user from base model"""
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_user_to_dict(self):
        """testing user experience to dict"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertTrue('email' in user_dict)
        self.assertTrue('password' in user_dict)
        self.assertTrue('first_name' in user_dict)
        self.assertTrue('last_name' in user_dict)

    def test_user_str(self):
        """testing definition of user string"""
        user = User()
        user_str = str(user)
        self.assertTrue('[User]' in user_str)
        self.assertTrue('id' in user_str)
        self.assertTrue('created_at' in user_str)
        self.assertTrue('updated_at' in user_str)
        self.assertTrue('email' in user_str)
        self.assertTrue('password' in user_str)
        self.assertTrue('first_name' in user_str)
        self.assertTrue('last_name' in user_str)


if __name__ == '__main__':
    unittest.main()
