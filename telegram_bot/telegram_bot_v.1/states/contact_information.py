from telebot.handler_backends import State, StatesGroup

class UserInfoState(StatesGroup):
    name = State()
    age = State()
    country = State()
    city = State()
    num_phone = State()