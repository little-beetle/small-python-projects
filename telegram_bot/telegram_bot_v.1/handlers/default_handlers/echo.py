from telebot.types import Message

from loader import bot

# @bot.message_handler(state=None)
# def bot_echo(message: Message):
#     bot.reply_to(
#         message, "Echo with no state or filter.\n" f"Message: {message.text}"
#     )