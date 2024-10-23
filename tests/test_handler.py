import unittest
from unittest.mock import Mock, patch, MagicMock
from app.handler import (
    is_message_valid, process_message, generate_response,
    clean_message_text, update_chat_history, send_response, message_handler
)


class TestHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.message = MagicMock()
        self.message.text = "Привет"
        self.message.chat = Mock()
        self.message.chat.id = 12345

    @patch('app.handler.chat_filter')
    def test_is_message_valid(self, mock_chat_filter) -> None:
        mock_chat_filter.check_all.return_value = True
        self.assertTrue(is_message_valid(self.message))
        mock_chat_filter.check_all.return_value = False
        self.assertFalse(is_message_valid(self.message))
        message = MagicMock()
        message.text = None
        self.assertFalse(is_message_valid(message))

    @patch('app.handler.process_message')
    @patch('app.handler.is_message_valid')
    def test_message_handler(
        self,
        mock_process_message,
        mock_is_message_valid
    ) -> None:
        mock_is_message_valid.return_value = True
        message_handler(self.message)
        mock_process_message.assert_called_with(self.message)

    @patch('app.handler.bot.send_chat_action')
    @patch('app.handler.generate_response')
    @patch('app.handler.send_response')
    def test_process_message(
        self,
        mock_send_response,
        mock_generate_response,
        mock_send_chat_action
    ) -> None:
        mock_generate_response.return_value = "Ответ"
        process_message(self.message)
        mock_send_chat_action.assert_called_with(12345, 'typing')
        mock_generate_response.assert_called_with(self.message)
        mock_send_response.assert_called_with(12345, "Ответ")

    @patch('app.handler.clean_message_text')
    @patch('app.handler.gpt_bot')
    def test_generate_response(
        self,
        mock_gpt_bot,
        mock_clean_message_text
    ) -> None:
        mock_clean_message_text.return_value = "Привет"
        mock_gpt_bot.invoke.return_value = "Ответ"
        self.assertEqual(generate_response(self.message), "Ответ")

    @patch('app.handler.clean_message_text')
    @patch('app.handler.gpt_bot')
    def test_generate_response_no_answer(
        self,
        mock_gpt_bot,
        mock_clean_message_text
    ) -> None:
        mock_clean_message_text.return_value = "Привет"
        mock_gpt_bot.invoke.return_value = None
        self.assertIsNone(generate_response(self.message))

    @patch('app.handler.bot_info')
    def test_clean_message_text(self, mock_bot_info) -> None:

        mock_bot_info.username = "BotName"
        self.message.text = "Привет @BotName"

        self.assertEqual(clean_message_text(self.message.text), "Привет ")

    @patch('app.handler.chat_storage')
    def test_update_chat_history(self, mock_chat_storage) -> None:
        update_chat_history("Привет", "user")
        mock_chat_storage.add_to_chat_history.assert_called_with({
            "role": "user",
            "content": "Привет",
            "largeContextResponse": False,
            "showHintForLargeContextResponse": False,
            "pluginId": None
        })

    @patch('app.handler.bot.send_message')
    def test_send_response(self, mock_send_message) -> None:
        send_response(12345, "Ответ")
        mock_send_message.assert_called_with(12345, "Ответ")


if __name__ == '__main__':
    unittest.main()
