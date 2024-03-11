import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Test suite for the console command interpreter."""

    def create_test_model(self, model_name):
        """Helper method to create models for testing."""
        create_cmd = f"create {model_name}"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(create_cmd)
            return f.getvalue().strip()

    def test_quit(self):
        """Test that 'quit' command exits the CLI."""
        with patch('sys.stdout', new_callable=StringIO) as f:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("quit")

    def test_EOF(self):
        """Test that EOF exits the CLI."""
        with patch('sys.stdout', new_callable=StringIO) as f:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("EOF")

    def test_create_missing_class(self):
        """Test 'create' command with missing class."""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_create_invalid_class(self):
        """Test 'create' command with invalid class."""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd("create MyClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_show_missing_class(self):
        """Test 'show' command with missing class."""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_show_missing_id(self):
        """Test 'show' command with missing id."""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_destroy_missing_class(self):
        """Test 'destroy' command with missing class."""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_all(self):
        """Test 'all' command with no class."""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd("all")
            self.assertIn('[', f.getvalue().strip())

    def test_update_missing_class(self):
        """Test 'update' command with missing class."""
        with patch('sys.stdout', new_callable=StringIO) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    # Add more tests for 'update', 'destroy' commands with valid and invalid inputs
    # Consider adding tests for the custom methods if you have implemented any in your console

class TestHBNBCommandUpdateDestroy(unittest.TestCase):
    """Testing update and destroy commands of the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """Set up test cases."""
        cls.console = HBNBCommand()

    def test_update_with_no_class_name(self):
        """Test 'update' with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_update_with_invalid_class_name(self):
        """Test 'update' with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update MyClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_update_with_no_id(self):
        """Test 'update' with missing instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_update_with_no_attribute_name(self):
        """Test 'update' with missing attribute name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234-1234-1234")
            self.assertEqual("** attribute name missing **", f.getvalue().strip())

    def test_update_with_no_value(self):
        """Test 'update' with missing value for the attribute."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234-1234-1234 email")
            self.assertEqual("** value missing **", f.getvalue().strip())

    def test_destroy_with_no_class_name(self):
        """Test 'destroy' with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_destroy_with_invalid_class_name(self):
        """Test 'destroy' with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy MyClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_destroy_with_no_id(self):
        """Test 'destroy' with missing instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    # Example for testing a custom method in the  console
    # def test_custom_method_valid_input(self):
    #     """Test custom method with valid input."""
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         self.console.onecmd("your_custom_method valid_input")
    #         self.assertIn("expected output", f.getvalue().strip())

    # def test_custom_method_invalid_input(self):
    #     """Test custom method with invalid input."""
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         self.console.onecmd("your_custom_method invalid_input")
    #         self.assertIn("expected error message", f.getvalue().strip())

if __name__ == '__main__':
    unittest.main()

