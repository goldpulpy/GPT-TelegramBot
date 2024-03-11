import unittest
from app.utils.chat_history import ChatHistory
from datetime import datetime, timedelta
import os

class TestChatHistory(unittest.TestCase):

    def setUp(self):
        self.chat_history = ChatHistory()
        self.chat_history_file_path = 'chat_history.json'
        
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

    def test_add_to_old_last_message(self):
        message = {"text": "Hello, world!"}
        self.chat_history.add_to_chat_history(message)
        self.chat_history.clear_time = datetime.now() - timedelta(minutes=40)
        self.chat_history.get_chat_history()
        self.chat_history.add_to_chat_history(message)
        self.assertEqual(self.chat_history.chat_history, [message])
        
 
    def tearDown(self) -> None:
        if os.path.isfile(self.chat_history_file_path):
            os.remove(self.chat_history_file_path)
    
if __name__ == '__main__':
    unittest.main()

