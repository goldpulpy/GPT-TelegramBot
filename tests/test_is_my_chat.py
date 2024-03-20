import unittest
from app.utils.is_my_chat import IsMyChat
from unittest.mock import Mock, patch, MagicMock

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

    def test_is_question_with_question(self):
        self.message.text = "Is this a question?"
        self.assertTrue(self.chat.is_question(self.message))

    def test_is_question_without_question(self):
        self.message.text = "This is not a question"
        self.assertFalse(self.chat.is_question(self.message))

    def test_check_all_true_conditions(self):
        self.message.text = "Is this your username?"
        self.chat.is_my_chat = MagicMock(return_value=True)
        self.chat.reply_to_me = MagicMock(return_value=False)
        self.chat.message_with_my_username = MagicMock(return_value=False)
        self.chat.is_question = MagicMock(return_value=True)
        self.assertTrue(self.chat.check_all(self.message))

    def test_check_all_false_conditions_not_my_chat(self):
        self.message.text ="This does not meet any conditions."
        self.chat.is_my_chat = MagicMock(return_value=False)
        self.chat.reply_to_me = MagicMock(return_value=False)
        self.chat.message_with_my_username = MagicMock(return_value=False)
        self.chat.is_question = MagicMock(return_value=False)
        self.assertFalse(self.chat.check_all(self.message))
    
    def test_check_all_false_conditions(self):
        self.message.text ="This does not meet any conditions."
        self.chat.is_my_chat = MagicMock(return_value=True)
        self.chat.reply_to_me = MagicMock(return_value=False)
        self.chat.message_with_my_username = MagicMock(return_value=False)
        self.chat.is_question = MagicMock(return_value=False)
        self.assertFalse(self.chat.check_all(self.message))
    
    
    def test_check_all_true_question(self):
        self.message.text = "Is this a question?"
        self.chat.is_my_chat = MagicMock(return_value=True)
        self.chat.reply_to_me = MagicMock(return_value=False)
        self.chat.message_with_my_username = MagicMock(return_value=False)
        self.chat.is_question = MagicMock(return_value=True)
        self.assertTrue(self.chat.check_all(self.message))
        
if __name__ == '__main__':
    unittest.main()