#!/usr/bin/python3
"""Test models for BaseModel class"""


import unittest
import os
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """tests for base model class"""

    def test_pep8_user(self):
        """check if class conforms pep8 quidelines"""
        style_pep = pep8.StyleGuide()
        file_result = style_pep.check_files(['models/user.py'])
        errs = file_result.get_statistics('E')
        error_messages = [f'{error[0]}:{error[1]}: {error[2]}'
                          for error in errs]

    def test_instance(self):
        """testing for type of class"""
        self.assertEqual(User, type(User()))
        person = User()
        self.assertIsInstance(person, BaseModel)

    def test_attr_id(self):
        """testing class type of id attribute"""
        self.assertEqual(str, type(User().id))

    def test_id_diff(self):
        base_1 = User()
        base_2 = User()
        base_3 = User()
        self.assertTrue(base_1.id != base_2.id)
        self.assertTrue(base_1.id != base_3.id)
        self.assertTrue(base_2.id != base_3.id)

    def test_attr_created_at(self):
        """testing type of created_at attribute"""
        self.assertEqual(datetime, type(User().created_at))

    def test_attr_updated_at(self):
        """testing type of updated_at attribute"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_attr_email(self):
        """testing type of emailattribute"""
        self.assertEqual(str, type(User().email))

    def test_attr_password(self):
        """testing type of password attribute"""
        self.assertEqual(str, type(User().password))

    def test_attr_first_name(self):
        """testing type of first_name attribute"""
        self.assertEqual(str, type(User().first_name))

    def test_attr_last_name(self):
        """testing type of updated_at attribute"""
        self.assertEqual(str, type(User().last_name))

    def test_attr_dict_empty(self):
        """empty dictionary"""
        dicts = {}
        base = User(**dicts)
        self.assertTrue(type(base.id) == str)
        self.assertTrue(type(base.created_at) == datetime)
        self.assertTrue(type(base.updated_at) == datetime)
        self.assertNotIn("__class__", base.__dict__.keys())

    def test_attr_dict_none(self):
        """None is passed"""
        bases = User(None)
        self.assertNotIn(None, bases.__dict__.values())

    def test_str(self):
        """checking output for __str__"""
        b_1 = User()
        self.assertEqual(b_1.__str__(), "[" + b_1.__class__.__name__ + "]"
                         " (" + b_1.id + ") " + str(b_1.__dict__))


class TestBaseModelSave(unittest.TestCase):
    """test class for save method"""

    def setUp(self):
        """method run ofor each test in class"""
        with open("tests.json", 'w'):
            FileStorage._FileStorage__file_path = "tests.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ destroys file for each test after running it"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("tests.json")
        except FileNotFoundError:
            pass

    def test_save1(self):
        """checking if updated_at times are different"""
        base_4 = User()
        old = base_4.updated_at
        base_4.save()
        new = base_4.updated_at
        self.assertLess(old, new)

    def test_save2(self):
        """test when none is passed"""
        base_5 = User()
        with self.assertRaises(TypeError):
            base_5.save(None)

    def test_save3(self):
        """test if instance is actually stored"""
        b_2 = User()
        b_2.save()
        b_id = "User." + b_2.id
        with open("tests.json", "r") as f:
            self.assertIn(b_id, f.read())


class TestToDict(unittest.TestCase):
    """tests for method to_dicts"""

    def test_dict_instance(self):
        """test if it is a dictionary"""
        base_6 = User()
        self.assertEqual(dict, type(base_6.to_dict()))

    def test_dict_type_attr(self):
        """checking class type for attributes"""
        base_7 = User()
        dicts = base_7.to_dict()
        self.assertTrue(type(dicts["created_at"] == str))
        self.assertTrue(type(dicts["updated_at"] == str))
        self.assertTrue(type(base_7.created_at) == datetime)
        self.assertTrue(type(base_7.updated_at) == datetime)
        self.assertEqual(dicts["created_at"], base_7.created_at.isoformat())
        self.assertEqual(dicts["updated_at"], base_7.updated_at.isoformat())

        # checking if keys exists
        self.assertIn("id", base_7.to_dict())
        self.assertIn("created_at", base_7.to_dict())
        self.assertIn("updated_at", base_7.to_dict())
        self.assertIn("__class__", base_7.to_dict())

    def test_attr_added(self):
        """check if attributes added to dict"""
        base_7 = User()
        base_7.first_name = "Alx"
        base_7.last_name = "school"
        base_7.email = "eve@gmail.com"
        base_7.password = "root"
        self.assertIn("first_name", base_7.to_dict())
        self.assertIn("last_name", base_7.to_dict())
        self.assertIn("email", base_7.to_dict())
        self.assertIn("password", base_7.to_dict())

    def test_not_same(self):
        """dicts created and self dict not same"""
        b_5 = User()
        self.assertNotEqual(b_5.to_dict(), b_5.__dict__)

    def test_wrong_type(self):
        """passing none"""
        b_0 = User()
        with self.assertRaises(TypeError):
            b_0.to_dict(None)
