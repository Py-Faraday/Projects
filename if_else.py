# '''
# if 7 < 6: 
# 	print('7 больше чем 6')
# else:
# 	print('7 меньше чем 6')
# '''
# '''
# a = 93 
# if a % 2 == 0:
# 	print('93 делится без остатка на 2')


# elif a % 3 == 0:
# 	print('93 делится без остатка на 3', a/3)
# '''
# '''

# age = int(input('введите ваш возраст: ')) 

# #int('18') => 18 

# if age >= 18:
# 	print('вы можете заходить')

# elif age < 18 and age > 12:
# 	print('ты подросток тебе нельзя')

# else:
# 	print('ты ребенок')
# '''

# '''
# a = 3**2

# b = 2**3

# if a > b:
# 	 print('a > b')
# elif a < b:
# 	print('a < b')
# else:
# 	print('a == b')

# '''
# '''
# a = int(input('введите число от 0 до 100:'))

# if a <= 21:
# 	print('Разрешено')

# elif a <= 57:
# 	print('Разрешено')

# else:
# 	print('Запрещено')
# '''
# '''

# a = int(input('Четное ли число?'))

# if a%2:[print('Не четное число')]

# else: 
# 	print('Четное числo',a)

# '''

# '''
# if True:
# 	print('True')

# '''
# '''
# a = 10//5 

# b = 10/5 

# if a == b:
# 	print('Равны', a, b)
# else:
# 	print('Не равны')

# '''
# '''

# a = int(input('введите цифру'))


# if a >0 :
# 	print(-a)
# else:
# 	print(a)
# '''
# '''
# a = 10 

# b = 5 

# if a>0 and b>0:
# 	print('Положителные')
# '''
# '''
# a = 10 

# b = 5 

# if a > b:
# 	print('a+2')
# else:
# 	print('b+2')
# '''
# '''
# a = int(input('ввести любое число>>>\n'))

# if a > 0:
# 	print('Положительное число')

# else:
# 	print('Отрицательное цисло')
# '''
# '''
# age = int(input('введите ваш возраст:'))

# if age >= 18:
# 	print('Совершеннолетний')

# elif age <= 18 and 4:
# 	print('Несовершоннелетний')

# '''
# '''
# a = 45

# b = 6 

# if a / b:
# 	print('Делиться')

# else:
# 	print('Не делиться')

# '''

# a = int(input('любой год:'))

# if a <= 2022:
# 	print('текущий год')

# elif a >= 0:
# 	print('год еще не наступил')

# else:
# 	print('год еще наступил')


# a = 12

# b = 13

# c = 14

# if a < b < c:
# 	print('верно',a , c)
# else:
# 	print('Не верно')


# a = 17391%17
# b = 546%17
# c = 934%17
# print(a,b,c)



# x = 13**172 

# if x > 0:
# 	print(x)


# hello = 'hello world'

# print('hello world'.upper())

# print ('HELLO WORLD'.lower())

# # a = 123
# print(bool(b))

# name = input('ваше имя?:')
# print('Здравствуйте {name},Вас приветствует ваш асистент!')

# age = input('сколько вам лет?:')
# print(age)

# a = input('Ваш любимый фильм?:')
# print('Неплохой фильм у вас хороший вкус')

# s = input('ввести символ')
# d =  'GitHub'
# print(d.split(s))


# a = ('хакеры слили в сеть данные пакистанской энергетической компании k-Electric')

# print(a.replace('е','3'))


# text = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
# print(len(text))

# text ='Самые важные собЫтия в миРе инфосека за сентябрь'
# s = '|'.join(text)
# print(s)

# text = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
# print(text.title()) 

#  login = Asan,password = 1234

# baza = {
#     'Admin':{
#         'name':'egida',
#         'password':'12312321'
#     }
# }
# klyouch = None
# while True:
#     table = input('1: Зарегистрироваться\n2: Авторизовться\n3: Информация\n4: Выход\n >>>')
#     if table == '1':    
#         if klyouch is None:
#             print('Добро пожаловать на регистратцию')
#             login = input('Введите логин: ')
#             name = input('Введите имя: ')
#             password = input('Придумайте пароль: ')
#             password1 = input('Подтвердите пароль: ')
#             while password != password1 or len(password) < 8:
#                 password = input('Пароль не должен быть не менее 8 символов\nПовторите ввод: ')
#                 password1 = input('Подтвердите пароль: ')
#             else:
#                 baza.update({
#                     login:{
#                         'name':name,
#                         'password':password
#                     }
#                 })
#                 print('Регистратция завершена')
#     elif table == '2':
#         if klyouch is None:
#             login = input('Введите свой логин: ')
#             password = input('Введите пароль: ')
#             if login in baza:
#                 if password == baza['Admin']['password']:
#                     print('Вы прошли Авторизатцию')
#                     klyouch = login
#                 else:
#                     print('Не верный пароль')
#             else:
#                 print('Мы не нашли пользователя в базе данных')
#         else:
#             print('Вы уже авторизованы')
#     elif table == '3':
#         if klyouch is not None:
#             print(f'''
#     Информация
#         Логин: {login}
#         Имя: {baza["Admin"]['name']}
#         Пароль:{baza["Admin"]['password']}''')
#         else:
#             print("Вы не акторизованы")
#     elif table == '4':
#         if klyouch is not None:
#             print('Вы вышли из авторизации')
#             klyouch = None
#     else:
#         print('Такой команды нет')


# text = '122223'
# print(text.isdigit())

# name = input('введите ваше имя:').lower()
# print(name) 


# text = ('мир труд май')
# print(text.title())


# num = input('Введите цифру:')
# if int (num) > 0:
#     if int(num) > 10:
#         print('Вы ввели цифру больше 10')
#         if int(num) >= 50:
#             print('Вы ввели цифру больше 50')
#     else:
#         print('Вы ввели меньше 10 но больше 0')
# elif int(num) < -10:
#     print('Вы ввели меньше -10')
# elif int(num) < 0:
#     print('Вы ввели меньше 0')


# num = (4)
# while(num > 0):
#     print('У нас',num,'столко имени')
#     num -= 1
# print('У нас не осталось ни одной цифры')



    