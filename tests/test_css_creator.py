import unittest
import os
from unittest.mock import patch
from css_creator import generate_css

class TestGenerateCSS(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_projects"
        os.makedirs(self.test_dir)

    def tearDown(self):
        # Remove the temporary directory after testing
        os.system(f"rm -rf {self.test_dir}")

    @patch('builtins.open', new_callable=open)
    def test_generate_css_success(self, mock_open):
        project_name = "css_project"
        project_path = os.path.join(self.test_dir, project_name)
        css_file = os.path.join(project_path, "styles.css")
        expected_file_content = "/* CSS */\n\nbody {\n  /* Styles */\n}"

        result = generate_css(os.path.join(self.test_dir, project_name))

        os.makedirs.assert_called_once_with(project_path)
        mock_open.assert_called_once_with(css_file, "w")
        mock_open().write.assert_called_once_with(expected_file_content)
        self.assertEqual(result, f"CSS project '{os.path.join(self.test_dir, project_name)}' created successfully!")

    # Add more test methods for other scenarios, such as edge cases

if __name__ == "__main__":
    unittest.main()
