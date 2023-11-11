#!/usr/bin/env python3
"""
This file contains state.py unit tests.
"""

import unittest
import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests instances and methods from state class
    """

    state = State()

    def test_class_existence(self):
        """Tests if the class exists.
        """
        self.assertEqual(str(type(self.state)), "<class 'models.state.State'>")

    def test_class_inheritance(self):
        """Tests if State is an instance of BaseModel.
        """
        self.assertTrue(self.state, BaseModel)

    def test_has_attributes(self):
        """Tests if the attributes exist.
        """
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_attributes_types(self):
        """Tests attributes types.
        """
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
