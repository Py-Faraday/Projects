from telebot import types

def buttons(titles: str)->object:
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.max_row_keys=3
    markup.row(*titles, 'back')
    return markup
def menu():
    return buttons(['1','2','3'])