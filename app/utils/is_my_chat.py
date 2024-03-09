from telebot.types import Message
from app import bot_info

class IsMyChat:
    def __init__(self, chat_id: int) -> None:
        self.chat_id = chat_id

    def is_my_chat(self, message: Message) -> bool:
        """
        Checks if the message is from the chat with the given chat_id.

        Args:
            message (Message): The message to check.

        Returns:
            bool: True if the message is from the chat with the given chat_id, 
            False otherwise.
        """
        return message.chat.id == self.chat_id
    
    def reply_to_me(self, message: Message) -> bool:
        """
        Replies to the message if it was sent by the bot.

        Args:
            message (Message): The message to check.

        Returns:
            bool: True if the message was sent by the bot, False otherwise.
        """
        
        if message.reply_to_message is not None:
            if message.reply_to_message.from_user.id == bot_info.id:
                return True
        return False
    
    def message_with_my_username(self, message: Message) -> bool:
        """
        Checks if the message contains the bot's username

        Args:
            message (Message): The message to check.

        Returns:
            bool:  True if the message contains the bot's username,
                   False otherwise.
        """
        my_username = f"@{bot_info.username}"
        if my_username in message.text:
            return True
        return False
    
    def is_question(self, message: Message) -> bool:
        """
        Checks if the message is a question.

        Args:
            message (Message): The message to check.

        Returns:
            bool: True if the message is a question, False otherwise.
        """
        return message.text.endswith("?")
        
    
    def check_all(self, message: Message) -> bool:
        """
        Checks if the message is from the chat with the given chat_id and
        was sent by the bot or contains the bot's username.
        
        Args:
            message (Message): The message to check.

        Returns:
            bool: True if the message is from the chat with the given chat_id and
            was sent by the bot or contains the bot's username, False otherwise.
        """
        
        if not self.is_my_chat(message):
            return False


        
        if  not self.reply_to_me(message) \
        and not self.message_with_my_username(message) \
        and not self.is_question(message):
            return False

        return True
        
        
        