from openai import RateLimitError

from chat_gpt.openai_functions import client
from .request_information import RequestInfoState
from loader import bot
from keyboards.inline.inline_cancel import get_cancel_button


@bot.message_handler(state=RequestInfoState.ask_question)
def get_answer_on_question(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": message.text}],
            temperature=0.1
        )
        bot.send_message(message.chat.id, completion.choices[0].message.content, reply_markup=get_cancel_button())
    except RateLimitError:
        bot.send_message(message.chat.id, "Что-то пошло не так, повторите свой вопрос", reply_markup=get_cancel_button())

