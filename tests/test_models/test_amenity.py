#!/usr/bin/python3
"""Unittest module for the Amenity Class."""


import unittest
import pep8
from datetime import datetime
from models.amenity import Amenity
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class Test_amenity_instances(unittest.TestCase):

    """ Unittest for testing the amnenity class"""

    def test_no_args(self):
        """tests for class type"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_id(self):
        """tests for id type"""
        self.assertEqual(str, type(Amenity().id))

    def test_two_amenities_unique_ids(self):
        """tests for unique ids"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_name_attr(self):
        """test fro name attribute"""
        self.assertEqual(str, type(Amenity().name))


class Test_amenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_name_attribute(self):
        """tests for name attribute"""
        a = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", a.__dict__)

    def test_pep8_base(self):
        """check if class conforms pep8 quidelines"""
        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['model/amenity.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]


if __name__ == "__main__":
    unittest.main()
