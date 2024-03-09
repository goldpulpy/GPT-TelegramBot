from app import bot, bot_info
from app.utils import loggerman
from app import handler

def main() -> None:
    """
    The main function that starts the bot.
    """
    
    # Log bot start
    loggerman.log(f"Bot started as {bot_info.username} ({bot_info.id})")

    # Start polling
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as err:
            loggerman.log(err)



if __name__ == "__main__":
    main()