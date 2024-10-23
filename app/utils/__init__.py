"""This module contains the utility classes."""
from config import CHAT_HISTORY_SIZE, CHAT_ID
from .chat_history import ChatHistory
from .is_my_chat import IsMyChat
from .gpt import GPT


chat_storage: ChatHistory = ChatHistory(CHAT_HISTORY_SIZE)
chat_filter: IsMyChat = IsMyChat(CHAT_ID)
gpt_bot: GPT = GPT()
