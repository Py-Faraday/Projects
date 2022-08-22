import telebot
from telebot import types
from config import TOKEN
from main import get_weather

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    with open('static/weather.tgs', 'rb') as sti:
        bot.send_sticker(message.chat.id, sti)

    text = "Я бот Погоды, Отправь назание города!!!"
    bot.send_message(message.chat.id, text)
    text = "Вы можете выбрать один из Вариантов городов"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Бишкек')
    item2 = types.KeyboardButton('Ош')
    item3 = types.KeyboardButton('Нью-Йорк')
    item4 = types.KeyboardButton('Антананариво')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        text = get_weather(message.text)
        bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)
