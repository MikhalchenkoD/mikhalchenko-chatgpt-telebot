from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from config_data.config import COMMANDS


def get_help_buttons():
    markup = InlineKeyboardMarkup(row_width=1)
    for command, desk in COMMANDS:
        markup.add(InlineKeyboardButton(text=desk, callback_data=command))
    return markup