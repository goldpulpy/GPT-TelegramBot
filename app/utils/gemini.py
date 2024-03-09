import requests
from app.prompt import PROMPT
from time import sleep

class Gemini:
    
    def __init__(
            self,
            temperature: float = 0.5,
            top_p: float = 1,
            max_tokens: int = 2000,
        ) -> None:
        """
        Initialize the GEMINI class.

        Parameters:
            temperature (float, optional): The temperature of the chat. Defaults to 0.5.
            top_p (float, optional): The top_p of the chat. Defaults to 1.
            max_tokens (int, optional): The max_tokens of the chat. Defaults to 2000.
        """
        # Initialize attributes
        self.url_base: str = "https://chat.googlegemini.co"
        # Initialize params
        self.params: dict = {
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens,
                "topP": top_p,
            },
            "safetySettings":[
                {"category":"HARM_CATEGORY_HARASSMENT","threshold":"BLOCK_NONE"},
                {"category":"HARM_CATEGORY_HATE_SPEECH","threshold":"BLOCK_NONE"},
                {"category":"HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold":"BLOCK_NONE"},
                {"category":"HARM_CATEGORY_DANGEROUS_CONTENT","threshold":"BLOCK_NONE"}
            ]
        }

    def invoke(self, messages: list = None) -> str:
        """
        Invoke the GEMINI API with the provided messages.

        Parameters:
            messages (list, optional): The messages to send to the GEMINI API. Defaults to None.

        Returns:
            str | dict: The response from the GEMINI API.
        """
        
        if messages is None or len(messages) == 0:
            return None
        
        
        self.__setup_params(messages)
        return self.__get_answer()
    
    def __setup_params(self, messages: list) -> None:
        """
        Setup the params for the GEMINI API.

        Args:
            messages (list): The messages to send to the GEMINI API.
        """
        messages.insert(0, {"role":"user","parts":[{"text":PROMPT}]})
        messages.insert(1, {"role":"model","parts":[{"text":"Хорошо"}]})
        self.params["contents"] = messages
    
    def __get_answer(self) -> str | None:
        """
        Get the answer from the GEMINI API.

        Returns:
            str | None: The answer from the GEMINI API.
        """

        api_path = "/api/google/v1beta/models/gemini-pro:streamGenerateContent"
        for _ in range(3):
            try:
                response = requests.post(
                    url=f"{self.url_base}{api_path}",
                    json=self.params,
                ).json()[0]
                    
                response = response.get("candidates", None)
                answer = response[0]["content"]["parts"][0]["text"]
                
                return answer
            except Exception:
                sleep(0.3)
                continue
        
        return None