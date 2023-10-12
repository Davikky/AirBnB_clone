#!/usr/bin/python3
"""This is a test file for the BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    A test suite for the BaseModel class

    This test case covers various aspects of the BaseModel class, including
    unique ID generation, attribute initialization, and methods like save
    and to_dict.
    """

    def setUp(self):
        """
        Set up test data and resources.

        This method is executed before each test method to initialize common
        test data and resources. It creates an instance of BaseModel.
        """
        self.name = 'BaseModel'
        self.instance = BaseModel()

    def test_unique_id(self):
        # Test if IDs are unique for each instance.

        another_instance = BaseModel()
        self.assertNotEqual(self.instance.id, another_instance.id)

    def test_created_at(self):
        # Test if created_at is set correctly

        self.assertIsNotNone(self.instance.created_at)

    def test_updated_at(self):
        # Test if updated_at is updated correctly by the save method

        original_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(original_updated_at, self.instance.updated_at)

    def test_to_dict(self):
        # Test if the to_dict method generates the correct dictionary.

        obj_dict = self.instance.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_default(self):
        """
        Test if the default instance creation produces an object
        of the expected type
        """

        i = BaseModel()
        self.assertEqual(type(i), BaseModel)


if __name__ == '__main__':
    unittest.main()
