# import telebot 
# from telebot import types


# from config import TOKEN 



# bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start'])
# def start(message):
#     text = 'hello world'
#     stk = open('static/hi.webp','rb')
    
    
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     but1 = types.KeyboardButton('Привет')
#     but2 = types.KeyboardButton('Как ты?')
#     but3 = types.KeyboardButton('foto')
#     but4 = types.KeyboardButton('random int')
#     but5 = types.KeyboardButton('audio')
#     markup.add(but1, but2,but3,but4,but5)
#     bot.send_message(message.chat.id, text,reply_markup=markup)
#     bot.send_sticker(message.chat.id, stk)
    
    
# @bot.message_handler(content_types=['text'])
# def com(message):
#     if message.chat.type == 'private':
#         if message.text == 'Привет':
#             text = 'Hello'
#             bot.send_message(message.chat.id, message.text)
#         elif message.text == 'Как ты?':
#             text = 'Хорошо,сам как?'
#             bot.send_message(message.chat.id, text)
#         elif message.text == 'foto':
#             photo = open('static/fire.jpg', 'rb')
#             bot.send_photo(message.chat.id, photo)
#         elif message.text == 'random int':
#             import random 
#             num = random.randrange(1,100)
#             bot.send_message(message.chat.id, num)
#         elif message.text == 'audio':
#             audio = open('static/fire.jpg', 'rb')
#             bot.send_audio(message.chat.id, audio)
#         else:
#             bot.send_message(message.chat.id, 'Неправильно ввели')
            
            
            
            
            
# bot.polling(non_stop=True)

