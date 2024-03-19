import unittest
from app.utils.gpt import GPT

class TestGPT(unittest.TestCase):
    """Test the GPT class."""
    
    def test_invoke_without_messages(self):
        """Test the invoke method without messages."""
        gpt = GPT()
        response = gpt.invoke()
        self.assertIsNone(response)

    def test_invoke_with_messages(self):
        """Test the invoke method with messages."""
        gpt = GPT()
        messages = [{
            "role": "user", 
            "content": "Hello, world!", 
            "pluginId": None
        }]
        response = gpt.invoke(messages=messages)
        self.assertIsNotNone(response)



if __name__ == '__main__':
    unittest.main()