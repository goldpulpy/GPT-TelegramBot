import unittest
from unittest.mock import patch
from app.utils.gpt import GPT

class TestGPT(unittest.TestCase):
    def setUp(self):
        self.gpt = GPT()

    def test_initialization(self):
        self.assertEqual(self.gpt.url_base, "https://chateverywhere.app")
        self.assertIn("model", self.gpt.params)
        self.assertIn("prompt", self.gpt.params)
        self.assertIn("temperature", self.gpt.params)

    @patch('app.utils.gpt.requests.post')
    def test_invoke_with_no_messages(self, mock_post):
        response = self.gpt.invoke()
        self.assertIsNone(response)
        mock_post.assert_not_called()

    @patch('app.utils.gpt.requests.post')
    def test_invoke_with_messages(self, mock_post):
        mock_post.return_value.text = "Test response"
        messages = ["Message 1", "Message 2"]
        response = self.gpt.invoke(messages)
        self.assertEqual(response, "Test response")
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertEqual(kwargs['url'], f"{self.gpt.url_base}/api/chat")
        self.assertIn('messages', kwargs['json'])
        self.assertEqual(kwargs['json']['messages'], messages)

    def test_setup_params(self):
        messages = ["Message 1", "Message 2"]
        self.gpt._GPT__setup_params(messages)
        self.assertIn("messages", self.gpt.params)
        self.assertEqual(self.gpt.params["messages"], messages)

if __name__ == '__main__':
    unittest.main()