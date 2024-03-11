#!/usr/bin/python3
"""
Test FileStorage for AirBnB_clone
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Define tests for FileStorage functionality."""

    def setUp(self):
        """Setup test case."""
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_new(self):
        """Test adding a new object to storage."""
        self.storage.new(self.model)
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test saving objects to file."""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test loading objects from file."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    @classmethod
    def tearDownClass(cls):
        """Clean up files (if any) created by the tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()

