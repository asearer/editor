import unittest
from unittest.mock import patch, MagicMock, call
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QTextEdit, QLineEdit, QMessageBox, QFileDialog, QInputDialog
from main_window import CodeEditor, TerminalEmulator, MainWindow

class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

    @patch('your_module.create_project')
    @patch('PyQt5.QtWidgets.QMessageBox.information')
    def test_create_project(self, mock_info, mock_create):
        window = MainWindow()
        window.create_project("Django")
        mock_create.assert_called_once_with("Django")
        mock_info.assert_called_once_with(window, "Project Created", "Django project created successfully.")

    @patch('PyQt5.QtWidgets.QFileDialog.getOpenFileName')
    def test_open_file_dialog(self, mock_getOpenFileName):
        mock_getOpenFileName.return_value = ("test_file.txt", "")
        window = MainWindow()
        window.open_file_dialog()
        self.assertEqual(window.editor.current_file, "File content")

    # You can add more test methods for other functionalities

class TestCodeEditor(unittest.TestCase):

    def test_open_file(self):
        editor = CodeEditor()
        editor.open_file("test_file.txt")
        self.assertEqual(editor.current_file, "File content")

    # Add more test methods for other functionalities

class TestTerminalEmulator(unittest.TestCase):

    @patch('subprocess.Popen')
    def test_execute_command(self, mock_popen):
        mock_process = MagicMock()
        mock_popen.return_value = mock_process
        widget = TerminalEmulator()
        widget.input_entry.setText("ls")
        widget.execute_command()
        mock_process.stdin.write.assert_called_once_with("ls\n")
        # Add more assertions for output updating

    # Add more test methods for other functionalities

if __name__ == "__main__":
    unittest.main()
