import telebot

bot = telebot.TeleBot("5851941623:AAHIS5BKwKSzo6Cn5I5TNRnTR5CVW2MfjDg")

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Hi, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Hello!", parse_mode="html")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your id {message.from_user.id}", parse_mode="html")
    elif message.text == "photo":
        photo = open("pause.svg", "rb")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "I don't understand you", parse_mode="html")
bot.polling(non_stop=True)