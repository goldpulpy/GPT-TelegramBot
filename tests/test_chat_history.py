import unittest
from unittest.mock import patch
from app.utils.chat_history import ChatHistory
from datetime import datetime, timedelta

class TestChatHistory(unittest.TestCase):
    def setUp(self):
        self.chat_history = ChatHistory(chat_size=2)

    def test_initialization(self):
        self.assertEqual(self.chat_history.chat_size, 2)
        self.assertEqual(len(self.chat_history.chat_history), 0)
        self.assertIsNone(self.chat_history.clear_time)

    def test_add_to_chat_history(self):
        self.chat_history.add_to_chat_history({"message": "Test 1"})
        self.assertEqual(len(self.chat_history.chat_history), 1)

    def test_ensure_chat_history_limit(self):
        self.chat_history.add_to_chat_history({"message": "Test 1"})
        self.chat_history.add_to_chat_history({"message": "Test 2"})
        self.chat_history.add_to_chat_history({"message": "Test 3"})
        self.assertEqual(len(self.chat_history.chat_history), 2)
        self.assertEqual(self.chat_history.chat_history[0], {"message": "Test 2"})
        self.assertEqual(self.chat_history.chat_history[1], {"message": "Test 3"})

    @patch('app.utils.chat_history.datetime')
    def test_clear_expired_chat_history(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2020, 1, 1, 12, 0, 0)
        self.chat_history.reset_clear_time()
        self.chat_history.add_to_chat_history({"message": "Test 1"})
        # Advance time beyond clear_time
        mock_datetime.now.return_value = datetime(2020, 1, 1, 12, 31, 0)
        self.chat_history.clear_expired_chat_history()
        self.assertEqual(len(self.chat_history.chat_history), 0)

    @patch('app.utils.chat_history.datetime')
    def test_reset_clear_time(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2020, 1, 1, 12, 0, 0)
        self.chat_history.reset_clear_time()
        self.assertEqual(self.chat_history.clear_time, datetime(2020, 1, 1, 12, 30, 0))

    def test_get_chat_history(self):
        self.chat_history.add_to_chat_history({"message": "Test 1"})
        history = self.chat_history.get_chat_history()
        self.assertEqual(history, [{"message": "Test 1"}])

if __name__ == '__main__':
    unittest.main()