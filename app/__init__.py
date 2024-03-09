from telebot import TeleBot
from telebot.types import User
from config import BOT_TOKEN

bot: TeleBot = TeleBot(BOT_TOKEN, num_threads=20)
bot_info: User = bot.get_me()