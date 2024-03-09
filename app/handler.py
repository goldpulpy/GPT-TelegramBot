from app import bot, bot_info
from app.utils import loggerman, gemini_bot
from app.utils import chat_filter, chat_storage

from telebot.types import Message


@bot.message_handler(content_types=['text'])
def message_handler(message: Message) -> None:
    """
    Handler for invoking the bot.

    Args:
        message (Message): The message from the user.
    """

    if message.text is None:
        return

    if not chat_filter.check_all(message):
        return
    
    query = message.text.replace(f"@{bot_info.username}", "")
    
    chat_storage.add_to_chat_history(
        {"role":"user","parts":[{"text": query}]}
    )
    messages = chat_storage.get_chat_history()
    answer_from_gemini = gemini_bot.invoke(messages)
    chat_storage.add_to_chat_history(
        {"role":"model","parts":[
                {"text": answer_from_gemini if answer_from_gemini else ""}
            ]
        }
    )
    
    if answer_from_gemini is None:
        loggerman.log("No answer from GEMINI API")
        return
    
    bot.send_message(message.chat.id, answer_from_gemini)
