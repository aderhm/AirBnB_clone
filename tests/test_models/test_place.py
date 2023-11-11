#!/usr/bin/env python3
"""
This file contains place.py unit tests.
"""

import unittest
import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Tests instances and methods from place class
    """

    place = Place()

    def test_class_existence(self):
        """Tests if the class exists.
        """
        self.assertEqual(str(type(self.place)), "<class 'models.place.Place'>")

    def test_city_inheritance(self):
        """Tests if Place is an instance of BaseModel.
        """
        self.assertTrue(self.place, BaseModel)

    def test_has_attributes(self):
        """Tests if the attributes exist.
        """
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))

    def test_attributes_types(self):
        """Tests attributes types.
        """
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertIsInstance(self.place.created_at, datetime.datetime)
        self.assertIsInstance(self.place.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
