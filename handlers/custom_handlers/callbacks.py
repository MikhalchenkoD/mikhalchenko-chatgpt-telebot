from loader import bot
from states.request_information import RequestInfoState

@bot.callback_query_handler(func=lambda call: call.data == 'cancel')
def delete_all_state(call):
    bot.delete_state(call.from_user.id, call.message.chat.id)
    bot.send_message(call.message.chat.id, 'Общение закончено')


@bot.callback_query_handler(func=lambda call: call.data == 'question')
def set_question_state(call):
    bot.set_state(call.from_user.id, RequestInfoState.ask_question ,call.message.chat.id)
    bot.send_message(call.message.chat.id, 'Бот готов ответить на вопрос')