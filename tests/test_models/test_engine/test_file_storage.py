"""
    module that test the file storage
"""

import unittest
import os
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
        # self.storage._FileStorage__file_path = "file_test.json"

    # def tearDown(self):
    #     if os.path.exists(self.storage._FileStorage__file_path):
    #         os.remove(self.storage._FileStorage__file_path)

    def test_type_all_storage(self):
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
        self.storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.assertTrue(key in self.storage._FileStorage__objects)
        self.assertTrue(self.storage._FileStorage__objects[key] == new_obj)

    def test_deserialization(self):
        """
            test deserialization of my __object attribute
        """
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        self.storage.new(obj_1)
        obj_before_serialization = self.storage._FileStorage__objects
        self.storage.save()
        self.storage.reload()
        obj_after_deserialization = self.storage._FileStorage__objects

        self.assertEqual(obj_before_serialization, obj_after_deserialization)
        self.assertEqual(type(obj_before_serialization),
                         type(obj_after_deserialization))
