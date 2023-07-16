#!/usr/bin/python3
"""Unittest module for the State Class."""


import unittest
from datetime import datetime
import time
from models.state import State
import re
import pep8
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class Test_state_instances(unittest.TestCase):
    """the test case for state class"""

    def test_no_args(self):
        """tests for class type"""
        self.assertEqual(State, type(State()))

    def test_conatins_all_instances(self):
        """tests for instance"""
        s = State()
        self.assertEqual(str(type(s)), "<class 'models.state.State'>")
        self.assertIsInstance(s, State)
        self.assertTrue(issubclass(type(s), BaseModel))

    def test_two_states_unique_ids(self):
        """tests for ids"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_contains_correct_keys(self):
        """tests for dicts"""
        s = State()
        self.assertIn("id", s.to_dict())
        self.assertIn("created_at", s.to_dict())
        self.assertIn("updated_at", s.to_dict())
        self.assertIn("__class__", s.to_dict())

    def test_pep8_base(self):
        """check if class conforms pep8 quidelines"""
        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['models/state.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]


if __name__ == "__main__":
    unittest.main()
