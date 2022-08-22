import telebot
from config import TOKEN



from main import button, menu

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=menu())


@bot.message_handler(content_types=['text'])
def r(message):
    if message.chat.type == "private":
        if message.text == "Персонажи":
            markup = button(get_character_names())
            bot.send_message(message.chat.id, "Выберите партнера", reply_markup=markup)

        elif message.text in get_character_names():
            bot.send_message(message.chat.id, get_character_text(message.text))
        
        elif message.text == "Локации":
            markup = button(get_location_names())
            bot.send_message(message.chat.id, "Выберите локацию", reply_markup=markup)
        elif message.text in get_location_names():
            bot.send_message(message.chat.id, parse_data(message.text))





        elif message.text == "|||":
            bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=menu())


bot.polling(none_stop=True)






