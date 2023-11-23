from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_cancel_button():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text='Завершить общение', callback_data='cancel'))
    return markup