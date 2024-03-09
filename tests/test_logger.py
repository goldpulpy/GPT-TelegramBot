import unittest
from unittest.mock import patch, mock_open
from datetime import datetime
from app.utils.logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()


    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_log_normal_no_start(self, mock_print, mock_open):
        self.logger.log("Test message")
        mock_open.assert_called_with(self.logger.output_file, 'a')
        mock_open().write.assert_called_with(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} - Test message\n")
        mock_print.assert_called_with(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} - Test message")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_log_normal_start(self, mock_print, mock_open):
        self.logger.log("Test message", is_start=True)
        mock_open.assert_called_with(self.logger.output_file, 'a')
        mock_open().write.assert_called_with(f"\n{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} - Test message\n")
        mock_print.assert_called_with(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} - Test message")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_log_empty_no_start(self, mock_print, mock_open):
        self.logger.log()
        mock_open.assert_called_with(self.logger.output_file, 'a')
        mock_open().write.assert_called_with(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} - \n")
        mock_print.assert_called_with(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} -")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_log_empty_start(self, mock_print, mock_open):
        self.logger.log(is_start=True)
        mock_open.assert_called_with(self.logger.output_file, 'a')
        mock_open().write.assert_called_with(f"\n{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} - \n")
        mock_print.assert_called_with(f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} -")

    def test_output_file(self):
        self.assertEqual(self.logger.output_file, 'logs.txt')




if __name__ == '__main__':
    unittest.main()