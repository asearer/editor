import unittest
from unittest.mock import patch, mock_open
import os
from html_creator import generate_html

class TestGenerateHTML(unittest.TestCase):

    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_html_success(self, mock_open, mock_makedirs):
        project_name = "my_project"
        expected_dir = os.path.join(os.getcwd(), project_name)
        expected_file_content = (
            "<!DOCTYPE html>\n"
            "<html>\n<head>\n<title></title>\n</head>\n"
            "<body>\n  <script src='script.js'></script>\n</body>\n"
            "</html>"
        )

        result = generate_html(project_name)

        mock_makedirs.assert_called_once_with(project_name)
        mock_open.assert_called_once_with(os.path.join(expected_dir, "index.html"), "w")
        mock_open().write.assert_called_once_with(expected_file_content)
        self.assertEqual(result, f"HTML project '{project_name}' created successfully!")

    # Add more test methods for other scenarios, such as failure cases

if __name__ == "__main__":
    unittest.main()
