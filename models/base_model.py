#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:

    # def __init__(self):
    #     self.id = str(uuid4())
    #     self.created_at = datetime.datetime.now()
    #     self.updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        if kwargs:
            if not isinstance(kwargs['created_at'], datetime):
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if not isinstance(kwargs['updated_at'], datetime):
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        copy_of_dict = self.__dict__.copy()
        print("copy", copy_of_dict)
        copy_of_dict['created_at'] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        copy_of_dict['updated_at'] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        copy_of_dict['__class__'] = self.__class__.__name__
        return copy_of_dict
