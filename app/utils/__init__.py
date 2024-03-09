from .logger import Logger
from .chat_history import ChatHistory
from config import CHAT_HISTORY_SIZE, CHAT_ID
from .is_my_chat import IsMyChat
from .gemini import Gemini


loggerman: Logger = Logger()
chat_storage: ChatHistory = ChatHistory(CHAT_HISTORY_SIZE)
chat_filter: IsMyChat = IsMyChat(CHAT_ID)
gemini_bot: Gemini = Gemini(temperature=1)