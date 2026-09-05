#!/usr/bin/python3
"""Tests for the BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def test_create_instance(self):
        """Test creating a BaseModel instance."""
        model = BaseModel()

        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_unique_ids(self):
        """Test that two instances have different IDs."""
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertNotEqual(model1.id, model2.id)

    def test_to_dict(self):
        """Test the dictionary representation."""
        model = BaseModel()
        model.name = "John"

        data = model.to_dict()

        self.assertEqual(data["__class__"], "BaseModel")
        self.assertEqual(data["name"], "John")
        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)

    def test_recreate_from_dict(self):
        """Test recreating an object from a dictionary."""
        model = BaseModel()
        model.name = "John"

        data = model.to_dict()
        new_model = BaseModel(**data)

        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.name, new_model.name)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)
        self.assertIsNot(model, new_model)


if __name__ == "__main__":
    unittest.main()
