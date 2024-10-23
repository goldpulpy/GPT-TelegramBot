"""This module contains the ChatHistory class."""
from datetime import datetime, timedelta
from app.utils.logger import setup_logger


logger = setup_logger(__name__)


class ChatHistory:

    def __init__(self, chat_size: int = 10) -> None:
        """
        Initialize the ChatHistory with a specified size.

        :param chat_size: The maximum size of the chat history.
        :type chat_size: int
        """
        self.chat_size = chat_size
        self.chat_history = []
        self.clear_time = None

    def get_chat_history(self) -> list:
        """
        Returns the chat history as a list of dictionaries.

        :return: A copy of the chat history.
        :rtype: list
        """
        self.clear_expired_chat_history()
        return self.chat_history.copy()

    def clear_expired_chat_history(self) -> None:
        """
        Clears the chat history if the clear time has expired.
        """
        if self.clear_time and datetime.now() > self.clear_time:
            logger.info("Clearing expired chat history")
            self.chat_history = []

    def add_to_chat_history(self, message: dict) -> None:
        """
        Adds a message to the chat history.

        :param message: The message to add to the chat history.
        :type message: dict
        """
        logger.debug("Adding message to chat history: %s", message)
        self.reset_clear_time()
        self.ensure_chat_history_limit()
        self.chat_history.append(message)
        logger.info(
            "Message added. Current chat history size: %d",
            len(self.chat_history)
        )

    def reset_clear_time(self) -> None:
        """
        Resets the time after which the chat history should be cleared.
        """
        self.clear_time = datetime.now() + timedelta(minutes=30)

    def ensure_chat_history_limit(self) -> None:
        """
        Ensures that the chat history does not exceed the specified size.
        """
        while len(self.chat_history) >= self.chat_size:
            self.chat_history.pop(0)
