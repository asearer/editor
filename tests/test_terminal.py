import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication, QTextEdit, QLineEdit, QVBoxLayout
from terminal import TerminalEmulator

class TestTerminalEmulator(unittest.TestCase):

    @patch('subprocess.Popen')
    @patch('platform.system')
    def test_command_execution(self, mock_system, mock_popen):
        mock_system.return_value = "Windows"
        mock_process = MagicMock()
        mock_popen.return_value = mock_process

        app = QApplication([])
        terminal = TerminalEmulator()

        terminal.input_entry.setText("test command")
        terminal.execute_command()

        mock_process.stdin.write.assert_called_once_with("test command\n")
        # Add more assertions as needed

    @patch('platform.system')
    def test_platform_detection(self, mock_system):
        mock_system.return_value = "Windows"
        app = QApplication([])
        terminal = TerminalEmulator()
        self.assertEqual(terminal.shell, "cmd.exe")

        mock_system.return_value = "Linux"
        terminal = TerminalEmulator()
        self.assertEqual(terminal.shell, "/bin/bash")
        # Add more assertions as needed

    # Add more test methods for other functionalities

if __name__ == "__main__":
    unittest.main()
