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
        print("----------", FileStorage.__objects)
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                json.load(file)
        except:
            return
