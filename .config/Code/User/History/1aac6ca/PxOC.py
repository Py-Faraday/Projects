from distutils.cmd import Command
from email import message
import telebot
from telebot import types

from config import TOKEN


bot=telebot.TeleBot(TOKEN)


@bot.message_handler(Commands=['start'])
def start(massege):
    text ='hello world'
    bot.send_message(message.chat.id,text)

bot.polling(non_stop=True)