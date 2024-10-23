"""This is the main file that starts the bot."""
from app import bot
from app.utils.logger import setup_logger
from app.handler import *

logger = setup_logger(__name__)


def main() -> None:
    """
    The main function that starts the bot.
    """

    # Start polling
    while True:
        try:
            logger.info("Starting bot...")
            bot.polling(none_stop=True)
        except Exception as err:
            logger.error("Error: %s", err)


if __name__ == "__main__":
    main()
