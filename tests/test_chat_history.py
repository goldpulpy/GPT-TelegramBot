import unittest
from app.utils.chat_history import ChatHistory
from unittest.mock import patch
import os, json


class TestChatHistory(unittest.TestCase):

    def setUp(self):
        self.chat_history = ChatHistory()
        self.chat_history_file_path = 'chat_history.json'
        
    def test_create_new_chat_history_file(self):
        self.assertTrue(os.path.isfile(self.chat_history_file_path))

    def test_load_chat_history(self):
        expected_chat_history = []
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value.__enter__().read.return_value = json.dumps(expected_chat_history)
            self.chat_history._ChatHistory__load_chat_history()
        
    def test_save_empty_chat_history(self):
        with patch('builtins.open', create=True) as mock_open:
            self.chat_history._ChatHistory__save_chat_history()
            mock_open.assert_called_once_with('chat_history.json', 'w')
            mock_open.return_value.__enter__().write.assert_called_once_with('[]')

    def test_save_non_empty_chat_history(self):
        self.chat_history.chat_history = ['Hello', 'How are you?']
        with patch('builtins.open', create=True) as mock_open:
            self.chat_history._ChatHistory__save_chat_history()
            mock_open.assert_called_once_with('chat_history.json', 'w')
            
    def test_add_single_message(self):
        message = {"user": "Alice", "text": "Hello"}
        self.chat_history.add_to_chat_history(message)
        self.assertEqual(self.chat_history.chat_history, [message])
    
    def test_add_multiple_messages(self):
        message1 = {"user": "Alice", "text": "Hello"}
        message2 = {"user": "Bob", "text": "Hi"}
        self.chat_history.add_to_chat_history(message1)
        self.chat_history.add_to_chat_history(message2)
        self.assertEqual(self.chat_history.chat_history, [message1, message2])
    
    def test_add_messages_at_max_capacity(self):
        self.chat_history.chat_size = 2
        message1 = {"user": "Alice", "text": "Hello"}
        message2 = {"user": "Bob", "text": "Hi"}
        message3 = {"user": "Alice", "text": "How are you?"}
        self.chat_history.add_to_chat_history(message1)
        self.chat_history.add_to_chat_history(message2)
        self.chat_history.add_to_chat_history(message3)
        self.assertEqual(self.chat_history.chat_history, [message2, message3])
    
    def tearDown(self) -> None:
        if os.path.isfile(self.chat_history_file_path):
            os.remove(self.chat_history_file_path)
    
if __name__ == '__main__':
    unittest.main()

