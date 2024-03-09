import unittest
from app.utils.is_my_chat import IsMyChat
from unittest.mock import Mock, patch

class TestIsMyChat(unittest.TestCase):
    def setUp(self) -> None:
        self.chat = IsMyChat(123)
        self.message = Mock()
        self.message.chat = Mock()
        self.message.reply_to_message = Mock()
        
    def test_is_my_chat_true(self):
        self.message.chat.id = 123
        self.assertTrue(self.chat.is_my_chat(self.message))

    def test_is_my_chat_false(self):
        self.message.chat.id = 456
        self.assertFalse(self.chat.is_my_chat(self.message))

    @patch('app.utils.is_my_chat.bot_info')
    def test_reply_to_me_true(self, mock_bot_info):
        mock_bot_info.id = 123
        self.message.reply_to_message.from_user.id = 123
        self.assertTrue(self.chat.reply_to_me(self.message))

    @patch('app.utils.is_my_chat.bot_info')
    def test_reply_to_me_false(self, mock_bot_info):
        mock_bot_info.id = 456
        self.message.reply_to_message = None
        self.assertFalse(self.chat.reply_to_me(self.message))


    @patch('app.utils.is_my_chat.bot_info')
    def test_message_with_my_username_true(self, mock_bot_info):
        mock_bot_info.username = "bot"
        self.message.text = f"Hello, @bot!"
        self.assertTrue(self.chat.message_with_my_username(self.message))

    @patch('app.utils.is_my_chat.bot_info')
    def test_message_with_my_username_false(self, mock_bot_info):
        mock_bot_info.username = "bot"
        self.message.text = "This is a regular message."
        self.assertFalse(self.chat.message_with_my_username(self.message))


if __name__ == '__main__':
    unittest.main()