import unittest
from unittest.mock import patch, mock_open
import os
from frontend_creator import generate_html, generate_css, generate_javascript, generate_react

class TestGenerateProjects(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_projects"
        os.makedirs(self.test_dir)

    def tearDown(self):
        # Remove the temporary directory after testing
        os.system(f"rm -rf {self.test_dir}")

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_html(self, mock_open):
        project_name = "html_project"
        expected_file_content = (
            "<!DOCTYPE html>\n"
            "<html>\n<head>\n<title></title>\n</head>\n"
            "<body>\n  <script src='script.js'></script>\n</body>\n"
            "</html>"
        )

        result = generate_html(os.path.join(self.test_dir, project_name))

        mock_open.assert_called_once_with(os.path.join(self.test_dir, project_name, "index.html"), "w")
        mock_open().write.assert_called_once_with(expected_file_content)
        self.assertEqual(result, f"HTML project '{os.path.join(self.test_dir, project_name)}' created successfully!")

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_css(self, mock_open):
        project_name = "css_project"
        expected_file_content = "/* CSS */\n\nbody {\n  /* Styles */\n}"

        result = generate_css(os.path.join(self.test_dir, project_name))

        mock_open.assert_called_once_with(os.path.join(self.test_dir, project_name, "styles.css"), "w")
        mock_open().write.assert_called_once_with(expected_file_content)
        self.assertEqual(result, f"CSS project '{os.path.join(self.test_dir, project_name)}' created successfully!")

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_javascript(self, mock_open):
        project_name = "javascript_project"
        expected_file_content = "// JavaScript\n\nconsole.log('Hello, World!');"

        result = generate_javascript(os.path.join(self.test_dir, project_name))

        mock_open.assert_called_once_with(os.path.join(self.test_dir, project_name, "script.js"), "w")
        mock_open().write.assert_called_once_with(expected_file_content)
        self.assertEqual(result, f"JavaScript project '{os.path.join(self.test_dir, project_name)}' created successfully!")

    def test_generate_react(self):
        # Mock os.system to prevent actual execution
        with patch('os.system') as mock_os_system:
            project_name = "react_project"

            result = generate_react(os.path.join(self.test_dir, project_name))

            mock_os_system.assert_called_once_with(f"npx create-react-app {os.path.join(self.test_dir, project_name)}")
            self.assertEqual(result, f"React project '{os.path.join(self.test_dir, project_name)}' created successfully!")

    # Add more test methods for other functionalities

if __name__ == "__main__":
    unittest.main()
