
import telebot
from telebot import types
from config import TOKEN
from maen import pop 

bot =telebot.TeleBot(TOKEN)
@bot.message_handler(commands=('start'))
def start(message):
    text='hello everyone,I am weather bot,send me your city name'
    bot.send_message(message.chat.id,text)

@bot.message_handler(content_types=['text'])
def lol(message):
    if message.chat.type=='private':
        text=pop(message.text)
        bot.send_message(message.chat.id,text)

bot.polling(non_stop=True)