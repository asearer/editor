import unittest
from unittest.mock import MagicMock, patch
from plugin_manager import PluginManager

class TestPluginManager(unittest.TestCase):

    @patch('os.listdir')
    @patch('importlib.util.spec_from_file_location')
    @patch('importlib.util.module_from_spec')
    def test_load_plugins(self, mock_module_from_spec, mock_spec_from_file_location, mock_listdir):
        # Mocking data
        mock_listdir.return_value = ["plugin1.py", "plugin2.py"]
        mock_plugin_module1 = MagicMock()
        mock_plugin_module2 = MagicMock()
        mock_module_from_spec.side_effect = [mock_plugin_module1, mock_plugin_module2]

        plugin_manager = PluginManager()
        plugin_manager.load_plugins()

        mock_listdir.assert_called_once_with("plugins")
        mock_spec_from_file_location.assert_any_call("plugin1", "plugins/plugin1.py")
        mock_spec_from_file_location.assert_any_call("plugin2", "plugins/plugin2.py")
        mock_module_from_spec.assert_any_call(mock_spec_from_file_location.return_value)
        mock_module_from_spec.assert_any_call(mock_spec_from_file_location.return_value)
        self.assertEqual(len(plugin_manager.plugins), 2)

    def test_run_plugins(self):
        plugin_manager = PluginManager()
        mock_plugin1 = MagicMock()
        mock_plugin2 = MagicMock()
        plugin_manager.plugins = [mock_plugin1, mock_plugin2]

        plugin_manager.run_plugins()

        mock_plugin1.run.assert_called_once()
        mock_plugin2.run.assert_called_once()

    # Add more test methods for other functionalities

if __name__ == "__main__":
    unittest.main()
