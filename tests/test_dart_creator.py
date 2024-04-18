import unittest
import os
from unittest.mock import patch
from dart_creator import create_project

class TestCreateProject(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_projects"
        os.makedirs(self.test_dir)

    def tearDown(self):
        # Remove the temporary directory after testing
        os.system(f"rm -rf {self.test_dir}")

    @patch('builtins.open', new_callable=open)
    def test_create_project_success(self, mock_open):
        project_name = "my_project"
        save_location = self.test_dir
        project_dir = os.path.join(save_location, project_name)
        lib_dir = os.path.join(project_dir, "lib")
        main_file = os.path.join(lib_dir, f"{project_name}.dart")

        result = create_project(project_name, save_location)

        os.makedirs.assert_called_once_with(project_dir, exist_ok=True)
        os.makedirs.assert_called_once_with(lib_dir, exist_ok=True)
        mock_open.assert_called_once_with(main_file, "w")
        mock_open().write.assert_called_once_with(f'void main() {{\n  print("Hello, {project_name}!");\n}}')
        self.assertEqual(result, f"Project '{project_name}' created successfully.")

    def test_create_project_missing_project_name(self):
        with self.assertRaises(ValueError) as context:
            create_project("", self.test_dir)

        self.assertEqual(str(context.exception), "Please enter a project name.")

    def test_create_project_missing_save_location(self):
        with self.assertRaises(ValueError) as context:
            create_project("my_project", "")

        self.assertEqual(str(context.exception), "Please select a save location.")

    # Add more test methods for other scenarios, such as edge cases

if __name__ == "__main__":
    unittest.main()
