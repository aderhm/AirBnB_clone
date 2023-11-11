#!/usr/bin/env python3
"""
This file contains review.py unit tests.
"""

import unittest
import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests instances and methods from review class
    """

    review = Review()

    def test_class_existence(self):
        """Tests if the class exists.
        """
        self.assertEqual(str(type(self.review)),
                         "<class 'models.review.Review'>")

    def test_class_inheritance(self):
        """Tests if Review is an instance of BaseModel.
        """
        self.assertTrue(self.review, BaseModel)

    def test_has_attributes(self):
        """Tests if the attributes exist.
        """
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_attributes_types(self):
        """Tests attributes types.
        """
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
