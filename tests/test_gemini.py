import unittest
from app.utils.gemini import Gemini

class TestGemini(unittest.TestCase):

    def test_initialization(self):    
        """Test the initialization and default parameter values."""
        gemini = Gemini()
        self.assertEqual(gemini.url_base, "https://chat.googlegemini.co")
        self.assertEqual(gemini.params['generationConfig']['temperature'], 0.5)
        self.assertEqual(gemini.params['generationConfig']['topP'], 1)
        self.assertEqual(gemini.params['generationConfig']['maxOutputTokens'], 2000)

    def test_custom_initialization(self):
        """Test initialization with custom parameter values."""
        gemini = Gemini(temperature=0.7, top_p=0.9, max_tokens=1500)
        self.assertEqual(gemini.params['generationConfig']['temperature'], 0.7)
        self.assertEqual(gemini.params['generationConfig']['topP'], 0.9)
        self.assertEqual(gemini.params['generationConfig']['maxOutputTokens'], 1500)

    def test_invoke_without_messages(self):
        """Test the invoke method without messages."""
        gemini = Gemini()
        response = gemini.invoke()
        self.assertIsNone(response)

    def test_invoke_with_messages(self):
        """Test the invoke method with messages."""
        gemini = Gemini()
        messages = [{"role": "user", "parts": [{"text": "Hello"}]}]
        response = gemini.invoke(messages=messages)
        self.assertIsNotNone(response)



if __name__ == '__main__':
    unittest.main()