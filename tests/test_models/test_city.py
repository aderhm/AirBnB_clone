"""
This file contains city.py unit tests.
"""

import unittest
import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests instances and methods from city class
    """

    city = City()

    def test_class_existence(self):
        """Tests if the class exists.
        """
        self.assertEqual(str(type(self.city)), "<class 'models.city.City'>")

    def test_city_inheritance(self):
        """Tests if City is an instance of BaseModel.
        """
        self.assertTrue(self.city, BaseModel)

    def test_has_attributes(self):
        """Tests if the attributes exist.
        """
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_attributes_types(self):
        """Tests attributes types.
        """
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertIsInstance(self.city.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
