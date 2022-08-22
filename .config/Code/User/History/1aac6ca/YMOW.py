
from ctypes import resize
from random import randrange
import telebot
from telebot import types

from config import TOKEN


bot=telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    text ='hello world'
    stk = open('static/hi.tgs','rb')


    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 =types.KeyboardButton('privet')
    button2 =types.KeyboardButton('kak dela')
    button3 = types.KeyboardButton('random int')
    
    # button3 =types
    markup.add(button1,button2,button3)
    bot.send_message(message.chat.id,text,reply_markup = markup)
    bot.send_sticker(message.chat.id,stk)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type.lower()=='private':
        if message.text =='privet':
            text='hello bro'
            bot.send_message(message.chat.id,text)
        elif message.text=='kak dela':
            text='otlichno sam kak '
            bot.send_message(message.chat.id,text)
        elif message.text =='random int':
            import random
            num =random.randrange(1,100)
            bot.send_message(message.chat.id,num)

bot.polling(non_stop=True)