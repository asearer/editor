import unittest
from unittest.mock import patch
import os
from project_management import ProjectManagement

class TestProjectManagement(unittest.TestCase):

    @patch('os.makedirs')
    @patch('os.path.exists')
    def test_create_project_success(self, mock_exists, mock_makedirs):
        mock_exists.return_value = False
        project_manager = ProjectManagement()
        project_name = "test_project"
        expected_path = os.path.join(os.getcwd(), project_name)

        result = project_manager.create_project(project_name)

        mock_makedirs.assert_called_once_with(expected_path)
        self.assertEqual(result, f"Project '{project_name}' created successfully at '{expected_path}'.")

    @patch('os.makedirs')
    @patch('os.path.exists')
    def test_create_project_failure(self, mock_exists, mock_makedirs):
        mock_exists.return_value = True
        project_manager = ProjectManagement()
        project_name = "existing_project"

        result = project_manager.create_project(project_name)

        mock_makedirs.assert_not_called()
        self.assertEqual(result, f"Project '{project_name}' already exists.")

    @patch('os.rmdir')
    @patch('os.path.exists')
    def test_delete_project_success(self, mock_exists, mock_rmdir):
        mock_exists.return_value = True
        project_manager = ProjectManagement()
        project_name = "existing_project"
        expected_path = os.path.join(os.getcwd(), project_name)

        result = project_manager.delete_project(project_name)

        mock_rmdir.assert_called_once_with(expected_path)
        self.assertEqual(result, f"Project '{project_name}' deleted successfully.")

    @patch('os.rmdir')
    @patch('os.path.exists')
    def test_delete_project_failure(self, mock_exists, mock_rmdir):
        mock_exists.return_value = False
        project_manager = ProjectManagement()
        project_name = "non_existing_project"

        result = project_manager.delete_project(project_name)

        mock_rmdir.assert_not_called()
        self.assertEqual(result, f"Project '{project_name}' does not exist.")

    # Add more test methods for other functionalities

if __name__ == "__main__":
    unittest.main()
