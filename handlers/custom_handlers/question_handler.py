from telebot.types import Message
from states.request_information import RequestInfoState
from loader import bot


@bot.message_handler(commands=["question"])
def ask_question_to_the_bot(message: Message):
    bot.set_state(message.from_user.id, RequestInfoState.ask_question, message.chat.id)
    bot.send_message(message.from_user.id, "Напишите свой вопрос")
