import json, os


class ChatHistory:
    
    def __init__(self, chat_size: int = 10) -> None:
        
        
        self.chat_size = chat_size
        self.chat_history = []
        self.__load_chat_history()
        
        
    def get_chat_history(self) -> list:
        """
        Returns the chat history as a list of dictionaries.
        """        
        return self.chat_history
    
    def __load_chat_history(self) -> None:
        """
        Loads the chat history from a JSON file.
        """
    
        if not os.path.isfile('chat_history.json'):
            with open('chat_history.json', 'w') as f:
                json.dump([], f, ensure_ascii=False)

        with open('chat_history.json') as f:
            self.chat_history = json.load(f)

    def __save_chat_history(self) -> None:
        """
        Saves the chat history to a JSON file.
        """
        with open('chat_history.json', 'w') as f:
            json.dump(self.chat_history, f, indent=4, ensure_ascii=False)
    
    
    def add_to_chat_history(self, message: dict) -> None:
        """
        Adds a message to the chat history.
        
        Args:
            message (dict): The message to add to the chat history.
        """

        if len(self.chat_history) >= self.chat_size:
            self.chat_history.pop(0)
            
        self.chat_history.append(message)
        self.__save_chat_history()