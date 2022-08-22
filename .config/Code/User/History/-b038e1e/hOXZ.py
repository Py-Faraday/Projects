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
    