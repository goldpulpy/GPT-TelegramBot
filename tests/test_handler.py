import unittest
from unittest.mock import Mock, patch, MagicMock
from app.handler import is_message_valid, process_message, generate_response, clean_message_text, update_chat_history, send_response
from telebot.types import Message


class TestHandler(unittest.TestCase):
    def setUp(self):
        self.message = MagicMock()
        self.message.text = "Привет"
        self.message.chat = Mock()
        self.message.chat.id = 12345

    @patch('app.handler.chat_filter')
    def test_is_message_valid(self, mock_chat_filter):
        mock_chat_filter.check_all.return_value = True
        self.assertTrue(is_message_valid(self.message))
        mock_chat_filter.check_all.return_value = False
        self.assertFalse(is_message_valid(self.message))

    @patch('app.handler.bot.send_chat_action')
    @patch('app.handler.generate_response')
    @patch('app.handler.send_response')
    def test_process_message(self, mock_send_response, mock_generate_response, mock_send_chat_action):
        mock_generate_response.return_value = "Ответ"
        process_message(self.message)
        mock_send_chat_action.assert_called_with(12345, 'typing')
        mock_generate_response.assert_called_with(self.message)
        mock_send_response.assert_called_with(12345, "Ответ")

    @patch('app.handler.clean_message_text')
    @patch('app.handler.update_chat_history')
    @patch('app.handler.gpt_bot')
    @patch('app.handler.chat_storage')
    def test_generate_response(
        self, 
        mock_chat_storage, 
        mock_gpt_bot, 
        mock_update_chat_history, 
        mock_clean_message_text
    ):
        mock_clean_message_text.return_value = "Привет"
        mock_gpt_bot.invoke.return_value = "Ответ"
        self.assertEqual(generate_response(self.message), "Ответ")


    @patch('app.handler.bot_info')
    def test_clean_message_text(self, mock_bot_info):
        
        mock_bot_info.username = "BotName"
        self.message.text = "Привет @BotName"
        
        self.assertEqual(clean_message_text(self.message.text), "Привет ")

    @patch('app.handler.chat_storage')
    def test_update_chat_history(self, mock_chat_storage):
        update_chat_history("Привет", "user")
        mock_chat_storage.add_to_chat_history.assert_called_with({
            "role": "user", 
            "content": "Привет",
            "largeContextResponse": False,
            "showHintForLargeContextResponse": False,
            "pluginId": None
        })

    @patch('app.handler.bot.send_message')
    def test_send_response(self, mock_send_message):
        send_response(12345, "Ответ")
        mock_send_message.assert_called_with(12345, "Ответ")


if __name__ == '__main__':
    unittest.main()