import unittest
from unittest.mock import patch
import os
from react_creator import generate_react

class TestGenerateReact(unittest.TestCase):

    @patch('os.system')
    def test_generate_react_success(self, mock_os_system):
        project_name = "my_project"
        expected_command = f"npx create-react-app {project_name}"
        generate_react(project_name)

        mock_os_system.assert_called_once_with(expected_command)

    # Add more test methods for other scenarios, such as failure cases

if __name__ == "__main__":
    unittest.main()
