import unittest
from unittest.mock import patch, mock_open
import os
from flask_creator import create_project

class TestCreateProject(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_projects"
        os.makedirs(self.test_dir)

    def tearDown(self):
        # Remove the temporary directory after testing
        os.system(f"rm -rf {self.test_dir}")

    @patch('builtins.open', new_callable=mock_open)
    def test_create_project_success(self, mock_open):
        project_name = "flask_project"
        save_location = self.test_dir
        expected_file_content = (
            "from flask import Flask\n\n"
            "app = Flask(__name__)\n\n"
            "@app.route('/')\n"
            "def index():\n"
            "    return 'Hello, Flask!'\n\n"
            "if __name__ == '__main__':\n"
            "    app.run(debug=True)"
        )

        result = create_project(project_name, save_location)

        mock_open.assert_called_once_with(os.path.join(self.test_dir, project_name, "app.py"), "w")
        mock_open().write.assert_called_once_with(expected_file_content)
        self.assertEqual(result, f"Flask project '{os.path.join(self.test_dir, project_name)}' created successfully!")

    def test_create_project_missing_project_name(self):
        with self.assertRaises(ValueError) as context:
            create_project("", self.test_dir)

        self.assertEqual(str(context.exception), "Please enter a project name.")

    def test_create_project_missing_save_location(self):
        with self.assertRaises(ValueError) as context:
            create_project("flask_project", "")

        self.assertEqual(str(context.exception), "Please select a save location.")

    # Add more test methods for other scenarios, such as edge cases

if __name__ == "__main__":
    unittest.main()
