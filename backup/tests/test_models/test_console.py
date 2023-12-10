import unittest
from unittest.mock import patch
from io import StringIO
from Airtrial.console import Console


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = Console()
        self.console.stdout = StringIO()  # Redirect stdout for testing

    def test_quit(self):
        with patch('sys.exit') as mock_exit:
            self.assertTrue(self.console.onecmd("quit"))
            mock_exit.assert_called_once()


if __name__ == '\x5f_main\x5f':
    unittest.main()
