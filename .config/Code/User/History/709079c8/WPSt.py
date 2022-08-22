import telebot

bot = telebot.TeleBot('5100051012:AAH6wsu1Hxc5C5vx0mg6fPx-PAMVrS7manY')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message == 'Привет':
        bot.send_message(message.from_user.id, 'Привет я бот, как твои дела?')
    elif message == '/help':
        bot.send_message(message.from_user.id, 'Напиши Привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю напиши мне просто Привет или /help')

bot.polling(none_stop=True, interval=0)