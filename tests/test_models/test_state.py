#!/usr/bin/python3
"""unittest cases for state"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """defining test case for state class"""

    def test_state_instance(self):
        """defining place instances"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIs(type(state), State)

    def test_state_attributes(self):
        """defining state attributes"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_inherits_from_base_model(self):
        """inheriting state from base model"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_state_to_dict(self):
        """testing state from dict"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertTrue('id' in state_dict)
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)
        self.assertTrue('name' in state_dict)

    def test_state_to_str(self):
        """testing state to string representations"""
        state = State()
        state_str = str(state)
        self.assertTrue('[State]' in state_str)
        self.assertTrue('id' in state_str)
        self.assertTrue('created_at' in state_str)
        self.assertTrue('updated_at' in state_str)
        self.assertTrue('name' in state_str)


if __name__ == '__main__':
    unittest.main()
