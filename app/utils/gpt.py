"""This module contains the GPT class."""
import requests
from app.prompt import get_prompt
from app.utils.logger import setup_logger


logger = setup_logger(__name__)


class GPT:
    """
    This class contains the methods to interact with the 
    ChatAverywhere API.
    """

    def __init__(self) -> None:
        """
        Initialize the GPT class.
        """
        self.url_base: str = "https://chateverywhere.app"
        self.params: dict = {
            "model": {
                "id": "gpt-3.5-turbo-0613",
                "name": "GPT-3.5",
                "maxLength": 12000,
                "tokenLimit": 4000,
                "completionTokenLimit": 2500,
                "deploymentName": "gpt-35"
            },
            "prompt": get_prompt(),
            "temperature": 0.5
        }

    def invoke(self, messages: list = None) -> str | None:
        """
        Invoke the ChatAverywhere API with the provided messages.

        :param messages: The messages to send to the ChatAverywhere API. 
        Defaults to None.
        :type messages: list
        :return: The response from the ChatAverywhere API.
        :rtype: str | None
        """

        if messages is None or len(messages) == 0:
            logger.warning("No messages provided to invoke GPT")
            return None
        logger.info("Invoking GPT with messages: %s", messages)
        self._setup_params(messages)
        response = self._get_answer()
        logger.debug("Received response from GPT: %s", response)
        return response

    def _setup_params(self, messages: list) -> None:
        """
        Setup the params for the ChatAverywhere API.

        :param messages: The messages to send to the ChatAverywhere API.
        :type messages: list
        """
        messages = messages.copy()
        self.params["messages"] = messages

    def _get_answer(self) -> str:
        """
        Get the answer from the ChatAverywhere API.

        :return: The answer from the ChatAverywhere API.
        :rtype: str
        """

        api_path = "/api/chat"
        response = requests.post(
            url=f"{self.url_base}{api_path}",
            json=self.params,
        ).text

        return response
