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
    if is_message_valid(message):
        process_message(message)

def is_message_valid(message: Message) -> bool:
    """
    Check if the message is valid and should be processed.

    Args:
        message (Message): The message to check.

    Returns:
        bool: True if the message should be processed, False otherwise.
    """
    if message.text is None:
        return False
    return chat_filter.check_all(message)

def process_message(message: Message) -> None:
    """
    Process the message by sending typing action, generating a response, and sending it back.

    Args:
        message (Message): The message to process.
    """
    bot.send_chat_action(message.chat.id, 'typing')
    response = generate_response(message)
    if response:
        send_response(message.chat.id, response)

def generate_response(message: Message) -> str:
    """
    Generate a response to the user's message.

    Args:
        message (Message): The user's message.

    Returns:
        str: The generated response.
    """
    query = clean_message_text(message.text)
    update_chat_history(query, "user")
    answer = gpt_bot.invoke(chat_storage.get_chat_history())
    if answer is None:
        loggerman.log("No answer from GPT bot")
        return None
    update_chat_history(answer, "assistant")
    return answer

def clean_message_text(text: str) -> str:
    """
    Clean the message text by removing the bot's username.

    Args:
        text (str): The text to clean.

    Returns:
        str: The cleaned text.
    """
    return text.replace(f"@{bot_info.username}", "")

def update_chat_history(content: str, role: str) -> None:
    """
    Update the chat history with a new message.

    Args:
        content (str): The content of the message.
        role (str): The role of the message sender (user or assistant).
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

    Args:
        chat_id (int): The chat ID to send the response to.
        response (str): The response to send.
    """
    bot.send_message(chat_id, response)