import telebot
from config import TOKEN
from main import button, menu
from product import get_product_names,get_product_text
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=menu())


@bot.message_handler(content_types=['text'])
def r(message):
    if message.chat.type == "private":
        if message.text == "Продукты":
            markup = button(get_product_names())
            bot.send_message(message.chat.id, "Выберите продукт", reply_markup=markup)
        elif message.text in get_product_names():
            
            bot.send_message(message.chat.id,get_product_text(message.text))
        elif message.text == "|||":
            bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=menu())


bot.polling(none_stop=True)






