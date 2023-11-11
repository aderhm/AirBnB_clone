"""
    model for testing BaseModel class
"""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        class for testing the class BaseModel
    """

    def setUp(self):
        """
            set up objects
        """
        self.my_model = BaseModel()
        self.my_second_model = BaseModel()

    def test_type_attr(self):
        """
            test the type and instances of attributes
        """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
        self.assertIsInstance(self.my_second_model.id, str)
        self.assertIsInstance(
            self.my_second_model.created_at, datetime.datetime)
        self.assertIsInstance(
            self.my_second_model.updated_at, datetime.datetime)

    def test_id(self):
        """
            test ids
        """
        self.assertNotEqual(self.my_model.id, self.my_second_model.id)

    def test_to_dict(self):
        """
            test the type of dict
        """
        self.assertEqual(type(self.my_model.to_dict()), dict)

    def test_class_attr_exist(self):
        """
            check if the key __class__ exist in object
        """
        self.assertIn('__class__', self.my_second_model.to_dict())

    def test_class_value(self):
        """
            test value of the key __class__
        """
        self.assertEqual(self.my_second_model.to_dict()[
                         '__class__'], self.my_second_model.__class__.__name__)

    def test_created_at(self):
        """
            test created_at of two objects
        """
        date1 = self.my_model.created_at
        date2 = BaseModel().created_at
        self.assertTrue(date1 < date2)

    def test_updated_at(self):
        """
            test updated_at after saving
        """
        new_model = BaseModel()
        date1 = new_model.updated_at
        new_model.save()
        date2 = new_model.updated_at
        self.assertTrue(date1 < date2)


if __name__ == '__main__':
    unittest.main()
