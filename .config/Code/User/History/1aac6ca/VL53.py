
from ctypes import resize
import telebot
from telebot import types

from config import TOKEN


bot=telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    text ='hello world'
    stk = open('static/hi.tg')
#     bot.send_message(message.chat.id,text)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type.lower()=='private':
        if message =='privet':
            text='hello bro'
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 =types.KeyboardButton('privet')
            button2 =types.KeyboardButton('kak dela')
            markup.add(button1,button2)
            bot.send_message(message.chat.id,text,reply_markup=markup)
        # bot.send_message(message.chat.id,text)
bot.polling(non_stop=True)