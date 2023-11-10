#!/usr/bin/env python3
import json
import importlib


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_obj] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        print("running reload")
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)

            for key, value in data.items():
                classNameString = key.split('.')[0]
                module_name = 'models.base_model'
                try:
                    module = importlib.import_module(module_name)
                    className = getattr(module, classNameString)
                except Exception as e:
                    print(e)
                FileStorage.__objects[key] = className(**value)
        except:
            return
