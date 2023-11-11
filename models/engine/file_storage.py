#!/usr/bin/env python3
"""
    Module handle the storage of objects I/O
"""
import json
import importlib


class FileStorage:
    """
        this class responsible of catch all object created from other
        modules and save it to json file
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            return all object stored in the class attribute __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            create a new format of the parameter obj and store it in __objects
        """
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_obj] = obj

    def save(self):
        """
            create a new dict and store inside it all object inside __objects
            and write the new dict to the json file
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
            this method will be run any time created new object
            and will be load all objects from json file
            also will be recreate the object class again
            by using the class name string
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

            for key, value in data.items():
                classNameString = key.split('.')[0]
                if classNameString == "BaseModel":
                    modulePath = 'models.base_model'
                elif classNameString == "User":
                    modulePath = 'models.user'

                module = importlib.import_module(modulePath)
                className = getattr(module, classNameString)

                FileStorage.__objects[key] = className(**value)
        except:
            return
