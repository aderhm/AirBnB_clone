"""
    module that test the file storage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
        class test the class FileStorage
    """

    def setUp(self):
        """
            set the storage
        """
        storage = FileStorage()
        self.storage = storage

    def test_all_storage(self):
        """
            test the return type
        """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_object(self):
        """
            test if the new object is added to attr __objects
        """
        new_obj = BaseModel()
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.storage.new(new_obj)
        self.assertTrue(key in self.storage._FileStorage__objects)
        self.assertTrue(self.storage._FileStorage__objects[key] == new_obj)
