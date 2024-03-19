import requests
from app.prompt import PROMPT

class GPT:
    def __init__(self) -> None:
        """
        Initialize the GPT class.
        """
        # Initialize attributes
        self.url_base: str = "https://chateverywhere.app"
        # Initialize params
        self.params: dict = {
            "model":{
                "id":"gpt-3.5-turbo-0613",
                "name":"GPT-3.5",
                "maxLength":12000,
                "tokenLimit":4000,
                "completionTokenLimit":2500,
                "deploymentName":"gpt-35"
                },
            "prompt": PROMPT,
            "temperature":0.5
            }
    def invoke(self, messages: list = None) -> str | None:
        """
        Invoke the ChatAverywhere API with the provided messages.

        Parameters:
            messages (list): The messages to send to the ChatAverywhere API. Defaults to None.

        Returns:
            str | None: The response from the ChatAverywhere API.
        """
        
        if messages is None or len(messages) == 0:
            return None
        
        
        self.__setup_params(messages)
        return self.__get_answer()
    
    def __setup_params(self, messages: list) -> None:
        """
        Setup the params for the ChatAverywhere API.

        Args:
            messages (list): The messages to send to the ChatAverywhere API.
        """
        messages = messages.copy()
        self.params["messages"] = messages
    
    def __get_answer(self) -> str:
        """
        Get the answer from the ChatAverywhere API.

        Returns:
            str: The answer from the ChatAverywhere API.
        """

        api_path = "/api/chat"
        response = requests.post(
            url=f"{self.url_base}{api_path}",
            json=self.params,
        ).text
            
        return response
