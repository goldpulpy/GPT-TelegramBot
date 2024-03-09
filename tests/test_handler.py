import unittest
from unittest.mock import patch, MagicMock
from app.handler import message_handler 

class TestBot(unittest.TestCase):


    @patch('app.bot.send_chat_action')
    @patch('app.bot.send_message')
    @patch('app.utils.gemini_bot.invoke')
    @patch('app.utils.chat_storage')
    @patch('app.utils.chat_filter.check_all')
    def test_message_handler(
            self, 
            mock_check_all, 
            mock_chat_storage, 
            mock_gemini_bot, 
            mock_send_message,
            mock_send_chat_action
    ):

        message = MagicMock()
        message.text = "Test message"
        message.chat.id = 12345

        # Setup the mocks
        mock_check_all.return_value = True  
        mock_gemini_bot.return_value = "Test response"
        # Call the message handler
        message_handler(message)

        mock_send_chat_action.assert_called_once_with(12345, 'typing')
        mock_send_message.assert_called_once_with(12345, "Test response")
    
    @patch('app.bot.send_message')
    def test_message_handler_not_my_chat(self,mock_send_message):
        
        message = MagicMock()
        message.text = "Test message"
        message.chat.id = 1234
        message_handler(message)
        mock_send_message.assert_not_called()
    
    @patch('app.bot.send_message')
    @patch('app.utils.chat_filter.check_all')
    def test_message_handler_empty_message(self, mock_send_message, mock_check_all):
        
        message = MagicMock()
        message.text = None
        message.chat.id = 1234
        mock_check_all.return_value = True  
        message_handler(message)

        mock_send_message.assert_not_called()
        


if __name__ == '__main__':
    unittest.main()