import os
from dotenv import load_dotenv

# Load .env and set environment variables
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

# Get environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN', None)
CHAT_ID = int(os.getenv('CHAT_ID', 0))
CHAT_HISTORY_SIZE = int(os.getenv('CHAT_HISTORY_SIZE', 10))
