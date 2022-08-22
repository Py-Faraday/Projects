import telebot 
from config import TOKEN
from button import buttons, menu
from python import get_info_title, det_info_text


bot = telebot.TeleBot(TOKEN)
 

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello World!', reply_markup=menu())

@bot.message_handler(content_types=['text'])
def tema(message):
    if message.chat.type=='private':
        if message.text=='1':
            markup=buttons(get_info_title())
            bot.send_message(message.chat.id, 'boom',reply_markup=markup)

        elif message.text in get_info_title():
            bot.send_message(message.chat.id, det_info_text(message.text,message.text))

        elif message.text == "back":
            bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=menu())


bot.polling(non_stop=True)