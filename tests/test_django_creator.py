import unittest
import os
from unittest.mock import patch
from django_creator import create_django_project

class TestCreateDjangoProject(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_projects"
        os.makedirs(self.test_dir)

    def tearDown(self):
        # Remove the temporary directory after testing
        os.system(f"rm -rf {self.test_dir}")

    @patch('os.makedirs')
    @patch('os.system')
    def test_create_django_project_success(self, mock_system, mock_makedirs):
        project_name = "django_project"
        directory = self.test_dir
        project_path = os.path.join(directory, project_name)
        app_path = os.path.join(project_path, project_name)

        result = create_django_project(project_name, directory)

        mock_makedirs.assert_called_once_with(project_path)
        mock_system.assert_called_once_with(f"django-admin startproject {project_name} --directory {project_path}")
        self.assertTrue(os.path.exists(app_path))
        self.assertTrue(os.path.exists(os.path.join(app_path, "__init__.py")))
        self.assertTrue(os.path.exists(os.path.join(app_path, "views.py")))
        self.assertEqual(result, f"Django project '{project_name}' created successfully!")

    # Add more test methods for other scenarios, such as edge cases

if __name__ == "__main__":
    unittest.main()
