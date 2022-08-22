
#'Задание №1': task1==================

# a=int(input('vvedite chislo 1:\n'))
# move=int(input('1:+\n2:-\n3:*\n4:/\n5:**\n'))
# b=int(input('vvedite chislo 2:\n'))
# if move==1:
#     rez=a+b
#     print(rez)
# elif move==2:
#     rez=a-b
#     print(rez)
# elif move==3:
#     rez=a*b
#     print(rez)
# elif move==4:
#     rez=a/b
#     print(rez)
# elif move==5:
#     rez=a**b
#     print(rez)
# else:
#     print('net takogo znaka')




# 'Задание №2' task1===================
# a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 89]
# a.append(13)
# b = a.count(13)
# v = len(a)
# s = b * 100 / v
# print(s)

# if s< 70:
#     print('Неужели')
# elif s >70:
#     print('Я так и знал')
# else:
#     print('Cовподение? Не думаю')





#'Задание №3':task1========================
# user = {
#     'egida':{
#         'password':'65',
#     }
# }
# key=None
# while True:
#     if key is None:
#         person = int(input('\n1:Зарегистрироваться'
#                     '\n2:Войти >>>'))

#         if person == 1:
#             login = input('Вводите логин: ')
#             password = input('Вводите пароль: ')
            
#             user.update({
#                 login:{'password':password}})
#             print('Успешно зарегистрировались!')
#             print(user)

#         if person == 2:
#             login =input('Вводите логин: ')
#             password =input('Вводите пароль: ')
            
#             if login in user and password == user[login]['password']:
#                 print('ДОБРО ПОЖАЛОВАТЬ')
#             else:
#                 print('НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ')




# 'Задание №1': task2====================
# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# for key ,value in dict1.items():
#     if value %3==0:
#         print(f'{key}={value} hi')
#     if value %5==0:
#         print(f'{key}={value} bye')




# 'Задание №2': task2========================
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in enumerate(languages):
#    print(i)



# 'Задание №3': task2=====================
# a=0
# for i in range(1,1000):
#     if i%3==0 or i%5==0:
#         a=a+i
# print(a)



# 'Задание №4': task2==================
# a="4729461084"
# c=0
# for i in range(len(a)):
#     c+=i
# print(c)


#'Задание №5':task2=====================

# from pprint import pprint
# date ={
#             "year": "2020",
#             "month": "10",
#             'day': '24',
#             'hour':'18',
#             'minut':'30'
#             }


# year = input('year:')
# month = (input('month:'))
# day = (input('day:'))
# hour = (input('hour:'))
# minut = (input('minut:'))


    
# date[year] = {
#       'year':year, 
#         'month':month,
#         'day':day,
#         'hour':hour,
#         'minut':minut
        
#     }    
    
# pprint(date)
# print(f'{year}-{month}-{day} {hour}:{minut}')


#'Задание №6': task2=====================
# c = ['anna', 'civic', 'kayak', 'mevel', 'madam', 'mom', 'noon', 'racecar', 'radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
# for i in c:
#     if i!=i[::-1]:
#         print("Не палиндром ", i)
#     else:
#         print("Палиндром ", i)




#final
# proverka=['Бишкек','Москва','Астана','Токио','Дели','Шанхай','Сан-Паулу','Мехико','Каир','Мумбаи','Пекин','Дакка','Осак','Армения','Нью Йорк','Карачи','Буэнос Айрес','Чунцин','Стамбул','Калькутта','Манила','Лагос','Тяньцзинь','Киншаса','Гуанчжоу','Лос Анджелес','Москва','Шэньчжэнь','Лахор','Бангалор','Париж','Богота','Джакарта','Ченнай','Лима','Бангкок','Сеул','Нагоя','Хайдарабад','Лондон','Тегеран','Чикаго','Чэнду','Нанкин','Ухань','Хошимин','Луанда','Ахмедабад','Куала Лумпур','Сиань','Гонконг','Дунгуань','Ханчжоу','Фошань','Шэньян','Багдад','Сантьяго','Сурат','Мадрид','Сучжоу','Пуна','Харбин','Хьюстон','Даллас','Торонто','Майами','Сингапур','Филадельфия','Атланта','Фукуока','Хартум','Барселона','Йоханнесбург','Санкт Петербург','Циндао','Далянь','Вашингтон']
# countries=['Бишкек','Москва','Астана','Нью Йорк']

# while True:
#     move=int(input('Выберите действие:\n1. Добавить новый город\n2. Отобразить список городов\n3. Заменить город\n4. Удалить город\n5. Выход'))
#     if move==1:
#         country=input('Введите название города:\n>>')
#         if country in countries:
#             print('Такой город уже есть!', country)
#         if country in proverka:
#             if country not in countries:
#                 countries.append(country)
#                 print('Город добавлен!')
#         else:
#             print('Некорректное название!')
#     if move==2:
#         print('Список городов:',countries)
#     if move==3:
#         this=input('Текущий город:\n>>')
#         for_this=input('Новый город:\n>>')
#         if this not in countries:
#             print('Текущий город отсутствует.')
#         if for_this in countries:
#             print('Такой город уже есть!')
#         if for_this in proverka:
#             if this in countries and for_this not in countries:
#                 countries.remove(this)
#                 countries.append(for_this)
#                 print('Город заменен.')
#         else:
#             print('Некорректное название!')
#         print(countries)
#     if move==4:
#         delete=input('Введите название города:\n>>')
#         if delete not in countries:
#             print('Текущий город отсутствует.')
#         else:
#             countries.remove(delete)
#             print('Город удален!')
#     if move==5:
#         print('Программа завершает работу.')
#         break
           