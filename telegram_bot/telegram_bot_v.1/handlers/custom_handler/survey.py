from keyboards.reply.contact import request_contact
from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message

@bot.message_handler(commands=["survey"])
def survey(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
    bot.send_message(message.from_user.id, f"Hi {message.from_user.username}, enter your name")

@bot.message_handler(state=UserInfoState.name)
def get_name(message: Message) -> None:
    if message.text.isalnum():
        bot.send_message(message.from_user.id, "Thank you, I write this info. Enter your age")
        bot.set_state(message.from_user.id, UserInfoState.age, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["name"] = message.text

    else:
        bot.send_message(message.from_user.id, "ERROR")


@bot.message_handler(state=UserInfoState.age)
def get_age(message: Message) -> None:
    if message.text.isdigit():
        bot.send_message(message.from_user.id, "Thank you, I write this info. Enter your country")
        bot.set_state(message.from_user.id, UserInfoState.country, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["age"] = message.text

    else:
        bot.send_message(message.from_user.id, "ERROR")


@bot.message_handler(state=UserInfoState.country)
def get_county(message: Message) -> None:
    bot.send_message(message.from_user.id, "Thank you, I write this info. Enter your country")
    bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["country"] = message.text


@bot.message_handler(state=UserInfoState.city)
def get_city(message: Message) -> None:
    bot.send_message(message.from_user.id,
                     "Thank you. I write this info. Now send your number phone click on button",
                     reply_markup=request_contact())

    bot.set_state(message.from_user.id, UserInfoState.num_phone, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["city"] = message.text


@bot.message_handler(content_types=["text", "contact"],state=UserInfoState.num_phone)
def get_contact(message: Message) -> None:
    if message.content_type == "contact":
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["num_phone"] = message.contact.phone_number
            text = f"Thank for the info :\n" \
                   f"Name --- {data['name']}\n" \
                   f"Age --- {data['age']}\n" \
                   f"Country --- {data['country']}\n" \
                   f"City --- {data['city']}\n" \
                   f"Contact --- {data['num_phone']}"
            bot.send_message(message.from_user.id, text)
    else:
        bot.send_message(message.from_user.id, "Сlick on the button to send the information")