from app import bot, bot_info
from app.utils import loggerman, gpt_bot
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
    
    bot.send_chat_action(message.chat.id, 'typing')
    
    query = message.text.replace(f"@{bot_info.username}", "")
    messages = chat_storage.get_chat_history()
    messages.append({"role": "user", "content": query, "pluginId": None})
    
    
    answer_from_gpt = gpt_bot.invoke(messages)
    if answer_from_gpt is None:
        loggerman.log("No answer from chataverywhere API")
        return
    
    chat_storage.add_to_chat_history(
        {"role": "user", "content": query, "pluginId": None}
    )
    chat_storage.add_to_chat_history({
        "role": "assistant", 
        "content": answer_from_gpt if answer_from_gpt is not None else "",  
        "largeContextResponse":False,
        "showHintForLargeContextResponse":False,
        "pluginId": None
        })
    bot.send_message(message.chat.id, answer_from_gpt)
