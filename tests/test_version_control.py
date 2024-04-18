import unittest
from unittest.mock import patch, MagicMock
import subprocess
from version_control import VersionControl

class TestVersionControl(unittest.TestCase):

    @patch('subprocess.run')
    def test_commit_changes_success(self, mock_run):
        mock_run.side_effect = [None, None]  # Mock successful runs of git commands
        version_control = VersionControl()

        result = version_control.commit_changes()

        mock_run.assert_any_call(["git", "add", "."])
        mock_run.assert_any_call(["git", "commit", "-m", "Commit message"])
        self.assertEqual(result, "Changes committed successfully.")

    @patch('subprocess.run')
    def test_commit_changes_failure(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, "git", output="Error message")  # Mock failed run of git command
        version_control = VersionControl()

        result = version_control.commit_changes()

        mock_run.assert_called_once_with(["git", "add", "."])
        self.assertIn("Error committing changes", result)

    @patch('subprocess.check_output')
    def test_get_commit_log_success(self, mock_check_output):
        mock_check_output.return_value = "Commit log content"  # Mock successful output of git log command
        version_control = VersionControl()

        result = version_control.get_commit_log()

        mock_check_output.assert_called_once_with(["git", "log"], stderr=subprocess.STDOUT, universal_newlines=True)
        self.assertEqual(result, "Commit log content")

    @patch('subprocess.check_output')
    def test_get_commit_log_failure(self, mock_check_output):
        mock_check_output.side_effect = subprocess.CalledProcessError(1, "git", output="Error message")  # Mock failed run of git log command
        version_control = VersionControl()

        result = version_control.get_commit_log()

        mock_check_output.assert_called_once_with(["git", "log"], stderr=subprocess.STDOUT, universal_newlines=True)
        self.assertIn("Error getting commit log", result)

    # Add more test methods for other functionalities

if __name__ == "__main__":
    unittest.main()
