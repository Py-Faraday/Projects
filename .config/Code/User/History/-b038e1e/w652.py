from unittest import result
import telebot
from telebot import types
from config import TOKEN
from main import varianat_game


bot =telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    text='Hello ,Davai poigraem'
    bot.send_message(message.chat.id, text)

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    item1 = types.KeyboardButton('👊🏻')
    item2 = types.KeyboardButton('✌🏻')
    item3 = types.KeyboardButton('✋🏻')
    markup.add(item1,item2,item3)
    text ='Vyberi deystvie'
    bot.send_message(message.chat.id,text,reply_markup==markup)

    @bot.message_handler(content_types=['text'])
    def dadada(message):
        if message.chat.id.type=='private':
            if message.text=='👊🏻':
                result==varianat_game(1)