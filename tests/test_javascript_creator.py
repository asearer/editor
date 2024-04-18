import unittest
from unittest.mock import patch, mock_open
import os
from javascript_creator import generate_javascript

class TestGenerateJavaScript(unittest.TestCase):

    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_javascript_success(self, mock_open, mock_makedirs):
        project_name = "my_project"
        expected_dir = os.path.join(os.getcwd(), project_name)
        expected_file_content = "// JavaScript\n\nconsole.log('Hello, World!');"

        result = generate_javascript(project_name)

        mock_makedirs.assert_called_once_with(project_name)
        mock_open.assert_called_once_with(os.path.join(expected_dir, "script.js"), "w")
        mock_open().write.assert_called_once_with(expected_file_content)
        self.assertEqual(result, f"JavaScript project '{project_name}' created successfully!")

    # Add more test methods for other scenarios, such as failure cases

if __name__ == "__main__":
    unittest.main()
