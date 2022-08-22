
import telebot
from telebot import types

from config import TOKEN


bot=telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    text ='hello world'
    bot.send_message(message.chat.id,text)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type.lower()=='private':
        if message =='privet':
            text='hello bro'
            bot.send_message(message.chat.id,text)
bot.polling(non_stop=True)