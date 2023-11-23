from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot
from keyboards.inline.inline_help import get_help_buttons


@bot.message_handler(commands=["help", "start"])
def bot_help(message: Message):
    bot.send_message(message.chat.id,
                     "Привет, я бот, с которым ты можешь пообщаться, задать вопрос или попросить совет",
                     reply_markup=get_help_buttons())
