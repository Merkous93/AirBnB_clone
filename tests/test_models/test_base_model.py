import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test the functionality of the BaseModel class."""

    def test_instance_creation(self):
        """Test creation of BaseModel instance."""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))

    def test_to_dict(self):
        """Test conversion of BaseModel instance to dictionary."""
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], my_model.id)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_from_dict(self):
        """Test initialization of BaseModel from dictionary."""
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, my_model.id)
        self.assertEqual(new_model.created_at, my_model.created_at)
        self.assertEqual(new_model.updated_at, my_model.updated_at)

if __name__ == '__main__':
    unittest.main()

