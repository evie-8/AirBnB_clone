#!/usr/bin/python3
"""Unittest module for the City Class."""


import pep8
import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class Test_city_instances(unittest.TestCase):
    """unittest for the class city"""

    def test_for_argument(self):
        """tests for classs type"""
        k = City
        self.assertEqual(City, type(k()))
        # self.assertIsInstance(k, City)

    def test_for_id(self):
        """tests for id type"""
        self.assertEqual(str, type(City().id))

    def test_for_two_cit_id(self):
        """tests for id uniqueness"""
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_attr_state_id(self):
        """test for attribute"""
        self.assertEqual(str, type(City().state_id))

    def test_attr_name(self):
        """test for attribute name"""
        self.assertEqual(str, type(City().name))


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_contains_coorect_keys(self):
        c = City()
        self.assertIn("id", c.to_dict())
        # self.aseertIn("created_at", c.to_dict())
        self.assertIn("__class__", c.to_dict())
        self.assertIn("updated_at", c.to_dict())

    def test_pep8_base(self):
        """check if class conforms pep8 quidelines"""

        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['models/city.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]


if __name__ == "__main__":
    unittest.main()
