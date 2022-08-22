import telebot
from config import TOKEN
from main import button, menu
from bots import get_character_names , get_character_text

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=menu())


@bot.message_handler(content_types=['text'])
def r(message):
    if message.chat.type == "private":
        if message.text == "Продукты":
            markup = button(get_character_names())
            bot.send_message(message.chat.id, "Выберите продукт", reply_markup=markup)

        elif message.text in get_character_names():
            bot.send_message(message.chat.id, get_character_text(message.text))
        elif message.text == "|||":
            bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=menu())


bot.polling(none_stop=True)






