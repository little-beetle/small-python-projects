from telebot.types import Message
import handlers
from config_data.config import DEFAULT_COMMAND
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMAND]
    bot.reply_to(message, "\n".join(text))