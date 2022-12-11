# a = ['eri', 'deku', 'Shoto', 'ria', 'nick']
# file = open('names.txt','a')
# for i in a :
#     file.write(i)
    
# file.close()

# with open('n.txt', 'r') as f:
#      print(f.read())
     
    
# with open('names.txt','w') as file:
#       for i in range(10) :
#           b = int(input('введи число:'))
# file.write(f'{b},')
# print('файл успешно завершен')


# a = ['wef','tgb','jon','wss']
# file = open ('n.txt','a')
# for i in a :
#      file.write(i)
    
# file.close


# a =''

# with open('img', 'w') as f:
#     f.write(a)
    


#  Task 2
# with open('users.txt','w') as file:
#     login = input('Введите логин:')
#     password = input('Введите пароль:')
#     file.write(login)
#     file.write(password)
#     print('Успешно написан')

# Task 3
# with open('users.txt','r') as file:
#     a = file.read()
#     if 'w' in a:
#         print('da est ')
#     else:
#         print('net')
        
    #  Task 4 
# t_words = {"dog", "cat", "mouse", "sheep"}
# file = open('python.txt', 'a')

# for i in t_words:
#     file.write(i)
# print(t_words)


# Task 5 
# name = ("Lyazat","Salavat", "Salavat","Daniyar")
# file = open('database.txt','w')
# print('Здравствуйте пользователь!')

# a = int(input('''
# 1.Войти
# 2.Зарегистрироваться
# >>>'''))

# if a == 1:
#         if name is not None:
#             login = input('Введите логин:')
#             password = int(input('Введите пароль'))
#             file.write(f'{name}\n')
            

# else:
#     print('Такой логин или пароль есть,авторизуйтесь!')
        
#     if a == 2:
#         if name is not None:
#             login = input('Введите логин:')
#             password = int(input('Введите пароль'))
#     else:
#         print('')
# file.close()










# a = ['Beka', 'Asyl', 'alan', 'rick', 'john', 'bob']
# file = open('names.txt', 'a')
# for i in a:
#      file.write(i)

# file.close()


# with open('python.txt', 'r') as f:
#      print(f.read())


# a = 'Hello world \n'
# with open('python.txt', 'w') as f:
#      f.write(a)


# with open('python.txt', 'a') as file:
#      login = input('Enter your login: ')
#      file.write('Логин: ')
#      file.write(login)
#      file.write('\n')
# print('Успешно создан файл с логином')


# names = ['Beka', 'Asyl', 'alan', 'rick', 'john', 'bob']
# with open('python.txt', 'w') as f:
#      for i in names:
#          f.write('\n')
#          f.write(str(names.index(i)))
#          f.write(' ')
#          f.write(i)
# print("Всё ок")


# with open('n.txt', 'w') as f:
#      for i in range(10):
#          b = int(input('Введи число: '))
#          f.write(f'{b},')
#          break
# print('Файл успешно записан')


# a = 'home/lessons/data/f'

# with open('img', 'w') as f:
#      f.write('data/foto.jpg')

# b = '../Изображения/linux.png'
# with open('n.txt', 'w') as f:
#     f.write(b)
# file = open('directories.txt', 'a')
