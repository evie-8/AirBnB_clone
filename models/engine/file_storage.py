#!/usr/bin/python3
"""Defines the class FileStorage"""


import json
from models.base_model import Basemodel


class FileStorage:
    """it is used as an abstract storage engine.
    Attributes:
    __file_path(str): name of the file to save the object to
    __objects: a dictonary
    """

    # def __init__(self):

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, ojb):
        """sets in __objects obj with the key <obj_class_name>.id"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        Filestorage.__object[k] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
    #  del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
