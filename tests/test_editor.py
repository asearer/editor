import unittest
from unittest.mock import patch
from editor import CodeEditor

class TestCodeEditor(unittest.TestCase):

    def setUp(self):
        self.editor = CodeEditor()

    def test_open_file(self):
        file_content = "This is a test file."
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = file_content
            self.editor.open_file("test_file.txt")
        self.assertEqual(self.editor.current_file, file_content)

    def test_save_file(self):
        file_content = "This is a test file."
        self.editor.current_file = file_content
        with patch('builtins.open', create=True) as mock_open:
            self.editor.save_file("test_file.txt")
            mock_open.assert_called_once_with("test_file.txt", "w")
            mock_open.return_value.__enter__.return_value.write.assert_called_once_with(file_content)

    def test_insert_text(self):
        initial_content = "Initial content."
        inserted_text = "Inserted text."
        expected_content = initial_content + inserted_text
        self.editor.current_file = initial_content
        self.editor.insert_text(inserted_text)
        self.assertEqual(self.editor.current_file, expected_content)

    def test_clear_editor(self):
        self.editor.current_file = "Some content."
        self.editor.clear_editor()
        self.assertEqual(self.editor.current_file, "")

if __name__ == "__main__":
    unittest.main()
