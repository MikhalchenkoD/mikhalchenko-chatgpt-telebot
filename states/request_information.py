from telebot.handler_backends import StatesGroup, State


class RequestInfoState(StatesGroup):
    ask_question = State()