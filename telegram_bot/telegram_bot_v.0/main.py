import telebot
from telebot import types
bot = telebot.TeleBot("5851941623:AAHIS5BKwKSzo6Cn5I5TNRnTR5CVW2MfjDg")

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Hi, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")
#
# @bot.message_handler(content_types=["text"])
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "Hello!", parse_mode="html")
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Your id {message.from_user.id}", parse_mode="html")
#     elif message.text == "photo":
#         photo = open("photo.jpg", "rb")
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "I don't understand you", parse_mode="html")


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "wow, cool photo!")


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("GitHub", url="https://github.com/little-beetle"))
    bot.send_message(message.chat.id, "Go to site", reply_markup=markup)



@bot.message_handler(commands=["help"])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("Website")
    start = types.KeyboardButton("Start")


    markup.add(website, start)
    bot.send_message(message.chat.id, "Go to site", reply_markup=markup)


bot.polling(non_stop=True)