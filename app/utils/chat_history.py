import json, os

from datetime import datetime, timedelta


class ChatHistory:
    
    def __init__(self, chat_size: int = 10) -> None:
        
        
        self.chat_size = chat_size
        self.chat_history = []
        self.clear_time = None
        
        
    def get_chat_history(self) -> list:
        """
        Returns the chat history as a list of dictionaries.
        """        
        return self.chat_history.copy()
    
    def add_to_chat_history(self, message: dict) -> None:
        """
        Adds a message to the chat history.
        
        Args:
            message (dict): The message to add to the chat history.
        """
        
        now_time = datetime.now()
        
        if self.clear_time is not None \
        and now_time > self.clear_time:
            self.chat_history = []



        self.clear_time = datetime.now() + timedelta(minutes=30)
        
        if len(self.chat_history) >= self.chat_size:
            self.chat_history.pop(0)
            
        self.chat_history.append(message)