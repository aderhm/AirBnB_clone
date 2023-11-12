"""
This file contains amenity.py unit tests.
"""

import unittest
import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class
    """

    amenity = Amenity()

    def test_class_existence(self):
        """Tests if the class exists.
        """
        self.assertEqual(str(type(self.amenity)),
                         "<class 'models.amenity.Amenity'>")

    def test_class_inheritance(self):
        """Tests if Amenity is an instance of BaseModel.
        """
        self.assertTrue(self.amenity, BaseModel)

    def test_has_attributes(self):
        """Tests if the attributes exist.
        """
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_attributes_types(self):
        """Tests attributes types.
        """
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
