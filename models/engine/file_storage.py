#!/usr/bin/env python3
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_obj] = obj

    def save(self):
        dict_to_store = {}
        for key, value in FileStorage.__objects.items():
            dict_to_store[key] = value.to_dict()
        with open(FileStorage.__file_path, 'a') as file:
            json.dump(dict_to_store, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                json.load(file)
        except:
            return
