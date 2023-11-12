"""
    module that test the file storage
"""

import unittest
import os
import json
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

    def test_instance(self):
        self.assertIsInstance(self.storage, FileStorage)

    def test_has_attr(self):
        """
            test if my object has the all methods
        """
        self.assertTrue(hasattr(self.storage, "all"))
        self.assertTrue(hasattr(self.storage, "new"))
        self.assertTrue(hasattr(self.storage, "save"))
        self.assertTrue(hasattr(self.storage, "reload"))

    def test_type_all_storage(self):
        """
            test the return type
        """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_all(self):
        """
            test if all object created by Base model
            insert in to __object attribute
        """
        obj_1 = BaseModel()
        obj_2 = BaseModel()

        key_obj_1 = "{}.{}".format(obj_1.__class__.__name__, obj_1.id)
        key_obj_2 = "{}.{}".format(obj_2.__class__.__name__, obj_2.id)

        all_objects = self.storage.all()

        self.assertIn(key_obj_1, all_objects.keys())
        self.assertIn(key_obj_2, all_objects.keys())
        self.assertIn(obj_1, all_objects.values())
        self.assertIn(obj_2, all_objects.values())

    def test_created_file(self):
        """
            test if the file created succesfully
            and the file have the expected key
        """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

        obj_1 = BaseModel()
        self.storage.save()

        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)

        self.assertIn('BaseModel.{}'.format(obj_1.id), data.keys())

    def test_reload_missing_file(self):
        """
            test missing file
        """
        self.assertRaises(FileNotFoundError, self.storage.reload())

    def test_empty_json(self):
        """
            test empty object
        """
        self.storage._FileStorage__objects = {}
        self.storage.save()
        self.storage.reload()
        object_reloaded = self.storage._FileStorage__objects
        self.assertEqual({}, object_reloaded)

    def test_new_object(self):
        """
            test if the new object is added to attr __objects
        """
        new_obj = BaseModel()
        # self.storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.assertTrue(key in self.storage._FileStorage__objects)
        self.assertTrue(self.storage._FileStorage__objects[key] == new_obj)

    def test_deserialization(self):
        """
            test deserialization of my __object attribute
        """
        BaseModel()
        obj_before_serialization = self.storage._FileStorage__objects
        self.storage.save()
        self.storage.reload()
        obj_after_deserialization = self.storage._FileStorage__objects

        self.assertEqual(obj_before_serialization, obj_after_deserialization)
        self.assertEqual(type(obj_before_serialization),
                         type(obj_after_deserialization))

    def test_reload(self):
        """
            test reload objects from file
        """
        obj_1 = BaseModel()
        self.storage.reload()
        object_reloaded = self.storage._FileStorage__objects
        self.assertIn('BaseModel.{}'.format(obj_1.id), object_reloaded)

    def test_save_BaseModel(self):
        """
            test for call save from BaseModel class
        """
        obj_1 = BaseModel()
        obj_1.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)

        self.assertIn('BaseModel.{}'.format(obj_1.id), data.keys())
