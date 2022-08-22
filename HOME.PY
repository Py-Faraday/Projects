# napitki = ['Пепси']
# vypechka = ['Булочка']
# jivachka = ['Ментос']
# syhofrukt = ['Орехи']
# frukty = ['Банан']
# ovoshi = ['Помидор']
# myaso = ['Говядина']
# while True:
#     tovary = napitki,vypechka,jivachka,syhofrukt,frukty,ovoshi,myaso 
#     table = int(input('\n1: Товары\n2: Добавить Товар\n3: Удалить товар\n4: Выход\n\[=-=]/: '))
#     if table == 1:
#         tovar = int(input('\n1: Напитки \n2: Выпечки \n3: Живачки \n4: Сухо-фрукты \n5: Фрукты \n6: Овощи \n7: Мясо \n8: Все товары\n\[-=-]/: '))
#         if tovar == 1:
#             print(napitki,"Всего",len(vypechka),"напиток")
#         elif tovar == 2:[print(vypechka,"Всего",len(vypechka),"выпичек")]
#         elif tovar == 3:[print(jivachka,"Всего",len(jivachka),"живачек")]
#         elif tovar == 4:[print(syhofrukt,"Всего",len(syhofrukt),"сухо-фруктов")]
#         elif tovar == 5:[print(frukty,"Всего",len(frukty),"фруктов")]
#         elif tovar == 6:[print(ovoshi,"Всего",len(ovoshi),"овощей")]
#         elif tovar == 7:[print(myaso,"Всего",len(myaso),"мяс")]
#         else:[print('Убедитесь что ввели правильную команду!')]
#     elif table == 2:
#         tovar = int(input('\n1: Добавить напиток \n2: Добавить выпечку \n3: Добавить живачку \n4: Добавить сухо-фрукт \n5: Добавить фрукт \n6: Добавить овощь \n7: Добавить мясо \n\[-=-]/: '))
#         if tovar == 1:
#             add_tovar = input('Введите название напитка: ')
#             napitki.append(add_tovar)
#         elif tovar == 2:
#             add_tovar = input('Введите название выпечки: ')
#             vypechka.append(add_tovar)
#         elif tovar == 3:
#             add_tovar = input('Введите название живачки: ')
#             jivachka.append(jivachka)
#         elif tovar == 4:
#             add_tovar = input('Введите название сухо-фрукта: ')
#             syhofrukt.append(syhofrukt)
#         elif tovar == 5:
#             add_tovar = input('Введите название фрукта: ')
#             frukty.append(frukty)
#         elif tovar == 6:
#             add_tovar = input('Введите название овоща: ')
#             ovoshi.append(ovoshi)
#         elif tovar == 7:
#             add_tovar = input('Введите название мясы: ')
#             myaso.append(myaso)
#         else:[print('Убедитесь что ввели правильную команду!')]
#     elif table == 3:
#         print('Панель для удаление, удаленные данные не подлежать востоновлении')
#         tovar = int(input('\n1: Удалить напиток \n2: Удалить выпечку \n3: Удалить живачку \n4: Удалить сухо-фрукт \n5: Удалить фрукт \n6: Удалить овощь \n7: Удалить мясо \n\[-=-]/: '))
#         if tovar == 1:
#             print(napitki),print(f"Убедитесь что вводите название правильно!")
#             delete_tovar  = input('\nНазвание товара: ')
#             napitki.remove(delete_tovar)
#         elif tovar == 2:
#             print(napitki),print("Убедитесь что вводите название правильно!")
#             delete_tovar  = input('\nНазвание товара: ')
#             vypechka.remove(delete_tovar)
#         elif tovar == 3:
#             print(napitki),print("Убедитесь что вводите название правильно!")
#             delete_tovar  = input('\nНазвание товара: ')
#             jivachka.remove(delete_tovar)
#         elif tovar == 4:
#             print(napitki),print("Убедитесь что вводите название правильно!")
#             delete_tovar = input('\nНазвание товара: ')
#             syhofrukt.remove(delete_tovar)
#         elif tovar == 5:
#             print(napitki),print("Убедитесь что вводите название правильно!")
#             delete_tovar = input('\nНазвание товара: ')
#             frukty.remove(delete_tovar)
#         elif tovar == 6:
#             print(napitki),print("Убедитесь что вводите название правильно!")
#             delete_tovar = input('\nНазвание товара: ')
#             ovoshi.remove(delete_tovar)
#         elif tovar == 7:
#             print(napitki),print("Убедитесь что вводите название правильно!")
#             delete_tovar = input('\nНазвание товара: ')
#             myaso.remove(delete_tovar)
#         else:[print('Убедитесь что ввели правильную команду!')]
#     elif table == 4:
#         print('Вы вышли из панели админа')
#         break
#     else:[print('Убедитесь что ввели правильную команду!')]
    
    
# my_list =[2, 4, 8]
# print(my_list[::-1])


# my_list = [2, 4, 8]
# my_list.reverse()
# print(my_list)


# def change(lst):
#     new_start = lst.pop()  # Удаляем последний элемент и сохраняем его в переменную
#     new_end = lst.pop(0)  # Удаляем первый элемент и сохраняем его в переменную
#     lst.append(new_end)  # Добавляем к списку новый последний элемент
#     lst.insert(0, new_start)  # Добавляем к списку новый первый элемент
#     return lst

# print(change([1, 2, 3]))
# print(change([1, 2, 3, 4, 5]))
# print(change(['н', 'л', 'о', 'с']))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# # Тесты
# print(change([1, 2, 3]))
# print(change([1, 2, 3, 4, 5]))
# print(change(['н', 'л', 'о', 'с']))


# def to_list(*args):
#     return list(args)

# print(to_list(1, 5, 77))
# print(to_list('Молоко', 5, '2020 год'))
# print(to_list([3, 4, 7], 8.3, True, 'Строка'))

# def useless(lst):
#     return max (lst) / len(lst)
# print(useless([1, 5, 77]))
# print(useless([19, 8.3, -4, 11, 0, 5]))
# print(useless([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))


# def list_sort(lst):
#     lst.sort(key=lambda x: abs(x), reverse=True)
#     return lst

# print(list_sort([1, 5, 77]))
# print(list_sort([19, 8.3, -4, 11, 0, 5]))
# print(list_sort([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))


# def all_eq(lst):
#     max_item = max(lst, key = lambda x: len(x))
# max_len = len(max_item)

# return lst[item.ljust( max_len, '_') for item in lst]

# print(all_eq(['крот', 'белка', 'выхухоль']))
# print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))  
# print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
 
 
# a = 17925 
# b = (34**2)
# print(a > b)


# a = 17925 
# b = (26*3)
# print(a > b)


# a = 17925 
# b = (17*33)
# print(a > b)



# a = 17925 
# b = (4394*4)
# print(a > b)


# a = 12
# b = 11
# c = 10
# print(a > b > c)


# a = (7 % 3 * 4,8)
# print(a)


# a = 11
# b = 11
# print(a == b)

# a = 1324
# b = 1465
# print(a != b)


# a = 12
# b = 13
# c = 14
# d = 193432
# print(a + b * c ** d)


# a = (17*3) 
# b = (12*5)
# print(a < b)


# a = (12**3)
# b = (13*7)
# print(a > b)


# a = (4**5) 
# b = (512+512)
# print(a == b)

# a = -21//10
# print(a)


# a = 22
# b = 100
# print(a/b)*100 


# a = 15
# b = 2 
# print(a + b)


# a = 15
# b = 2
# print(a - b)


# a = 25
# b = 75
# c = 10
# d = 95
# print((a+b+c+d)/4)

# a = 40
# b = 10
# c = 6
# d = 17
# e = 46
# print(a-e**(b/d))%c


# a = 4.7
# b = 4.7
# c = 4.7
# print(a+b*c)


# a = 2**3
# b = 3**2
# if a <= b:
#     print('verno')
# else:
#     print('ne verno')
    
    
# a = int(input('введите число от 0 до 100:'))

# if a <= 21:
#  	print('Разрешено')

# elif a <= 57:
#  	print('Разрешено')
  
# else:
#  	print('Запрещено')
  
# d = {
#     '1':3,
#     'list':[1,2,3],
#     'name':{'Bob Marley': '+777555888',
#     'Nicky Romeri':'+996777222111',
#     'Ricky Whittle': +996777666444}
# }

# print(d['name']['Bob Marley'])
# print(d['name']['Ricky Whittle'])
# print(d['name']['Nicky Romeri'])



# users = {
#     'Admin':{
#         'name':'admin',
#         'phone':'996555444333',
#         'balance':500000,
#         'password':'12312321',
#     },
#     'Argen':{
#         'name':'Argen',
#         'phone':'999580780',
#         'balance':5000,
#         'password':'12312321',
#     }
# }
# key = None
# while True:
#     print('Здраствуйте уважаемый клиент!')
#     m = int(input('''
#     1 Заарегистрироваться 
#     2 Авторизоваться 
#     3 Перевод баланса
#     4 Список пользователей 
#     5 Информатция 
#     6 Изменить логин
#     7 Изменить пароль
#     8 Выход из банка
#     >>> '''))
#     if m == 1:
#         if key is None:
#             login = input('введите логин ')
#             name = input('введите полное ваше имя ')
#             phone = int(input('введите ваш номер +996'))
#             password = input('Придумайте пароль ')
#             password1 = input('Подтвердите пароль ')
#             while password != password1 and len(password) < 8:
#                 password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
#                 password1 = input('Повторите пароль ')
            
#             else:
#                 print('Регистратция прошла ждем ответа базы\n')
#                 key = login
#                 f = open('База вашего банка.txt','a+')
#                 f.write(f'\nУзер {key} создал новый аккаунт\n') 
#                 f.close()
#                 users.update({
#                     login :{
#                         'name':name,
#                         'phone':phone,
#                         'balance':1000,
#                         'password':password,
#                     }
#                 })
#                 print('Регистратьсия успешно!\n')
#     elif m == 2:    
#         if key is None:
#             print('Добро пожаловать в авторизацию ')
#             login = input('Введите логин ')
#             password = input('введите пароль ')
#             if login in users:
#                 if password == users[login]['password']:
#                     key = login
#                     if key is not None:    
#                         f = open('База вашего банка.txt','a+')
#                         f.write(f'\nУзер {key} вошел в свой аккаунт\n') 
#                         f.close()
#                         print('Вы авторизовались ')
#                     else:[print('Не корекное авторизация')]
#                 else:[print('Не верный пароль')]
#             else:[print('Нет такого пользователя ')]
#         else:[print('Вы уже авторизованы ')]
#     elif m == 3:
#         if users is not None:
#             loginP = input('Введите имя получателя ')
#             summa = int(input('введите сумму перевода '))
#             if loginP in users:
#                 if summa <= users[key]['balance']:
#                     f = open('База вашего банка.txt','a+')
#                     f.write(f'\nУзер {key} отправил {summa} сомов узеру {loginP}\n') 
#                     f.close()
#                     users[key]['balance'] -= summa
#                     users[loginP]['balance']+= summa
#                     f = open('База вашего банка.txt','a+')
#                     f.write(f'\nУзер {loginP} получил {summa} сомов от узера {key}\n') 
#                     f.close()
#                     print('Перевод успешен')
#                 else:[print('У вас не достаточно денег')]
#             else:[print('такого пользователя нет')]
#         else:[print('вы не авторизованы')]
#     elif m == 4:
#         if key is not None:
#             print(users)
#             f = open('База вашего банка.txt','a+')
#             f.write(f'Узер {key} посмотрел всех пользователей банка\n') 
#             f.close()
#     elif m == 5:
#         if key is not None:
#             print(f'''
#             Логин: {users["Admin"]}
#             Имя: {users["Admin"]['name']}
#             Номер телефона: {users["Admin"]['phone']}
#             Баланс: {users["Admin"]['balance']}
#             \n''')
#             f = open('База вашего банка.txt','a+')
#             f.write(f'Узер {key} отправил запрос на свои данные\n') 
#             f.close()
#         else:[print('вы не авторизованы')]
#     elif m == 6:
#         if key is not None:
#             print(f'\nВаш login: {login}\n')
#             new_login = input('Введите новый логин: ')
#             f = open('База вашего банка.txt','a+')
#             f.write(f'\nУзер {login} Изменил свой логин на {new_login}\n') 
#             f.close()
#             login = new_login
#             print(f'Логин успешно обновлён на {login}')
#         else:[print('вы не авторизованы')]
#     elif m == 7:
#         if key is not None:
#             print(f'\nВаш пароль: {users["Admin"]["password"]}\n')
#             password = input('Введите текуший пароль: ')
#             if password == users[key]['password']:
#                 print('Пароль должен быть не менее 8 сиволов \n')
#                 password = input('Введите новый пароль: ')
#                 password1 = input('Подтвердите новый пароль: ')
#                 f = open('База вашего банка.txt','a+')
#                 f.write(f'\nУзер {key} изменил свой пароль на {users[login]["password"]}\n') 
#                 f.close()
#                 while password != password1 and len(password) < 8:
#                     password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
#                     password1 = input('Подтвердите новый пароль ')
#                 else:
#                     users.update({
#                         login :{
#                             'name':name,
#                             'phone':phone,
#                             'balance':1000,
#                             'password':password
#                         }
#                     })
#                     f = open('База вашего банка.txt','a+')
#                     f.write(f'\nУзер {key} изменил свой пароль на {users[login]["password"]}\n')
#                     f.close()
#             else:[print('Извините пароль не верный')]
#         else:[print('вы не авторизованы')]
#     elif m == 8:
#         print('Приходите ещё ')
#         break
#     else:[print('Брат такой команды нет')]
    


# a = ['d','s','w','t','d','F','k']
# a.append(34)
# a.append(32)

# print(a)

# i = 5000
# while i > 1000:
#      print(i) 
#      i /= 2
     

# for j in 'hello world':
#     if j == 'w':
#         continue
#     print(j * 2, end = '')
    

# count = 12
# word = "Hello World!"
# for i in word:
#     if i == "w":
#         count += 1

# print("Count:", count)


# i = 34
# while i <= 67:
#      if i / 2 != 1:
#          print(i)
#          i += 2


# a = 'hello world','wgudj',345
# print(a)


# a = dict(oaisjd=123, q3rds=23456)
# print(a)


# a = dict.fromkeys(['a','b','d'], 2)
# print(a)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = list(set(a) & set(b))
# print(result)



# a = int(input('Выберите: \n1:+\n2:-\n3:*\n4:%\n5:/\n6:** \n>>> '))
# b = int(input('Выберите число>>> '))
# c = int(input('Выберите число>>> '))
# if a == 1:
#     d = b+c
#     print(d)
# elif a == 2:
#     d = b-c
#     print(d)
# elif a == 3:
#     d = b * c 
#     print(d)
# elif a == 4:
#     d = b % c 
#     print(d)
# elif a == 5: 
#     d = b / c
#     print(d)
# elif a == 6: 
#     d = b ** c
#     print(d)
# else:
#     print('Такого знака нет!!!')
     


# def func(x):
#     def add (w):
#         return x + w
#     return add 

# test = func (200) 
# print(test(234)) 

# def off(x):
#     def see(q):
#         return x * q
#     return see

# s = off(2000)
# print(s(2))


# for i in 'see':
#     if i == 'w':
#         break
# else:   
#         print('нету')


# a = {12,34,56,78,55}
# b = 12
# print(b in a)


# a = {12,34,56,78,55}
# b = {13,45,23,78}
# print(a.isdisjoint(b))


# a = {12,34,56,78,55}
# b = {13,34,56,78,55}
# print(a == b)
            
# rec(a)


