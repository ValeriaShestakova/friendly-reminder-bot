import logging
import os
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers.reminder_bot import start, echo


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)


def main():
    try:
        telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    except KeyError as exc:
        logging.exception(f"Required environment variable {exc} is not set.")
        sys.exit(1)

    updater = Updater(telegram_bot_token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == main():
    main()
