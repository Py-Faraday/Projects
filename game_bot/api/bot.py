import telebot 
from telebot import types
from config import TOKEN 
from main import pop

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    text = 'Hello friends,i weather bot,send me your sity name'
    bot.send_message(message.chat.id, text)
    
@bot.message_handler(content_types=['text'])
def com(message):
    if message.chat.type == 'private':
        text = pop(message.text)
        bot.send_message(message.chat.id, text)
        
bot.polling(none_stop=True)

    