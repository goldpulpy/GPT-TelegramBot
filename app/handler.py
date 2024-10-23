"""This module contains the message handler for the bot."""
from telebot.types import Message

from app import bot, bot_info
from app.utils import gpt_bot
from app.utils import chat_filter, chat_storage
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


@bot.message_handler(content_types=['text'])
def message_handler(message: Message) -> None:
    """
    Handler for invoking the bot.

    :param message: The message from the user.
    :type message: Message
    """
    logger.info("Received message: %s", message.text)
    if is_message_valid(message):
        process_message(message)


def is_message_valid(message: Message) -> bool:
    """
    Check if the message is valid and should be processed.

    :param message: The message to check.
    :type message: Message
    :return: True if the message should be processed, False otherwise.
    :rtype: bool
    """
    if message.text is None:
        logger.warning("Received message with no text")
        return False
    valid = chat_filter.check_all(message)
    logger.debug("Message validity: %s", valid)
    return valid


def process_message(message: Message) -> None:
    """
    Process the message by sending typing action, generating a response, and 
    sending it back.

    :param message: The message to process.
    :type message: Message
    """
    logger.info("Processing message from chat ID: %d", message.chat.id)
    bot.send_chat_action(message.chat.id, 'typing')
    response = generate_response(message)
    if response:
        send_response(message.chat.id, response)
    else:
        logger.warning("No response generated for message: %s", message.text)


def generate_response(message: Message) -> str:
    """
    Generate a response to the user's message.

    :param message: The user's message.
    :type message: Message
    :return: The generated response.
    :rtype: str
    """
    query = clean_message_text(message.text)
    update_chat_history(query, "user")
    answer = gpt_bot.invoke(chat_storage.get_chat_history())
    if answer is None:

        return None
    update_chat_history(answer, "assistant")
    return answer


def clean_message_text(text: str) -> str:
    """
    Clean the message text by removing the bot's username.

    :param text: The text to clean.
    :type text: str
    :return: The cleaned text.
    :rtype: str
    """
    return text.replace(f"@{bot_info.username}", "")


def update_chat_history(content: str, role: str) -> None:
    """
    Update the chat history with a new message.

    :param content: The content of the message.
    :type content: str
    :param role: The role of the message sender (user or assistant).
    :type role: str
    """
    chat_storage.add_to_chat_history({
        "role": role,
        "content": content,
        "largeContextResponse": False,
        "showHintForLargeContextResponse": False,
        "pluginId": None
    })


def send_response(chat_id: int, response: str) -> None:
    """
    Send the generated response to the user.

    :param chat_id: The chat ID to send the response to.
    :type chat_id: int
    :param response: The response to send.
    :type response: str
    """
    bot.send_message(chat_id, response)
