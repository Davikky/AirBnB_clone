#!/usr/bin/python3
"""This is a test file for the BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test case for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a fresh instance of BaseModel for each test.
        """

        self.instance = BaseModel()

    def test_init_with_kwargs(self):
        """
        Test BaseModel instance creation with **kwargs.

        Checks if a BaseModel instance can be created using **kwargs
        and validates that attributes are correctly initialized.
        """

        data = {
            'name': 'Test Instance',
            'value': 42,
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.name, data['name'])
        self.assertEqual(instance.value, data['value'])

    def test_save_updates_updated_at(self):
        """
        Test if the save method correctly updates 'updated_at'.
        """

        original_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(original_updated_at, self.instance.updated_at)

    def test_unique_id(self):
        """
        Test if IDs are unique for each instance.
        """

        another_instance = BaseModel()
        self.assertNotEqual(self.instance.id, another_instance.id)

    def test_created_at_is_set(self):
        """
        Test if created_at is set correctly.
        """

        self.assertIsNotNone(self.instance.created_at)

    def test_updated_at_is_updated_by_save(self):
        """
        Test if updated_at is updated correctly by the save method.
        """

        original_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(original_updated_at, self.instance.updated_at)

    def test_to_dict_generates_expected_representation(self):
        """
        Test if the to_dict method generates the expected dictionary
        representation.
        """

        obj_dict = self.instance.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_default_instance_creation(self):
        """
        Test if the default instance creation produces an object of the
        expected type.
        """

        i = BaseModel()
        self.assertIsInstance(i, BaseModel)


if __name__ == '__main__':
    unittest.main()
