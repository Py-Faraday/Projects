# from random import choice

# students = ['Каныкей', 'Бексултан', 'Айбарчын', 'Тилек', 'Арген', 
#   'Байзак', "Актан", "Эгида", "Бэйл", "Нурдоолот", 'Искен']

# team1 = []
# team2 = []


# while len(team1) != 6:
#   name = choice(students)
#   if name not in team1:
#     team1.append(name)

# while len(team2) != 5:
#   name = choice(students)
#   if name not in team1 and name not in team2:
#     team2.append(name)
    
# print('Команда 1', team1)    
# print('Команда 2', team2)



# 'Задания 3'tasks1

# user = {
#     'egida':{
#         'login':'78347',
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
#                 print('hello')
#             else:
#                 print('no')




# Задания 5 tasks2
            
# from pprint import pprint            



# date ={
#             'year': '2020',
#             'month': '10',
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



# tasks1 Задания 1
# a = int(input('Введите число 1:\n'))
# move = int(input('1:+\n2:-\n3:*\n4:/\n5:**\n'))
# b = int(input('Введите число2:\n'))
# if move == 1:
#      rez = a+b
#      print(rez)
# elif move == 2:
#      rez = a-b
#      print(rez)
# elif move == 3:
#      rez = a*b
#      print(rez)
# elif move == 4:
#      rez = a/b
#      print(rez)
# elif move == 5:
#      rez = a**b
#      print(rez)
# else:
#      print('Нет такого знака!')
 
# tasks1 2 

# a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# a.append(13)
# b = a.count(13)
# v = len(a)
# s = b * 100 / v
# print(s)

# if s< 70:
#      print('Неужели')
# elif s >70:
#      print('Я так и знал')
# else:
#      print('Cовподение? Не думаю')
    
# tasks2 1
# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# for key ,value in dict1.items():
#      if value %3 == 0:
#          print(f'{key}={value} hi')
#      if value %5 == 0:
#          print(f'{key}={value} bye')


# tasks2 2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in enumerate(languages):
#     print(i)


# tasks2 3
# a = 0
# for i in range(1,1000):
#      if i % 3 == 0 or i % 5 == 0:
#          a = a + i
# print(a)


# tasks2 4      

# a = "4729461084"
# c = 0
# for i in range(len(a)):
#      c += i
# print(c)     


# Черновик
# d = "98765456"
# c = 0
# for i in range(len(d)):
#     c += i
# print(c)
        
        
# tasks2 6
# a = ['anna', 'civic', 'kayak', 'mevel', 'madam', 'mom', 'noon', 'racecar', 'radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
# for i in a:
#      if i != i[::-1]:
#          print("Не палиндром ", i)
#      else:
#          print("Палиндром ", i)
         




        

        

               

        

        









