import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication
import sys
from src.main_window import MainWindow
import main  # assuming main.py contains the main function

class TestMain(unittest.TestCase):

    @patch('main.QApplication')
    @patch('main.MainWindow')
    @patch('main.sys.exit')
    def test_main(self, mock_exit, mock_main_window, mock_qapplication):
        mock_app_instance = MagicMock()
        mock_qapplication.return_value = mock_app_instance

        main.main()

        mock_qapplication.assert_called_once_with(sys.argv)
        mock_main_window.assert_called_once_with()
        mock_main_window_instance = mock_main_window.return_value
        mock_main_window_instance.show.assert_called_once_with()
        mock_app_instance.exec_.assert_called_once_with()
        mock_exit.assert_called_once_with(mock_app_instance.exec_.return_value)

if __name__ == "__main__":
    unittest.main()
