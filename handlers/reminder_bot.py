from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text("It's so nice to talk with an intelligent person!")
    update.message.reply_text(update.message.text)
