# try:
#     set1 = set()
#     for i in range(5):
#         a = int(input('Введите число: '))
#         set1.add(a)
# except ValueError as y:
#     print(f'У вас такая вот ошибка{y}')
# except NameError as y:
#     print(f'У вас такая вот ошибка{y}')
# print(min(set1))
    


# values = ['adam', '74955645', 787, ['set','dict'], {'set is set'}]
# values_2 = []
# for i in values:
#     try:
#         set(i)
#         values_2.append(True)
        
#     except:
#         values_2.append(False)


# print(values_2)



# python = input('Введите функцию пайтон: ')

# try:
#     eval(python)
# except:
#     print('netu')


# users = []
# while True:
#     user = int(input('Введите сумму: '))
#     if user > 50000:
#         b = user / (3.47 * 100)
#         c = round(b, 2)
#         users.append(c)
#         print(users)
# else:
#         print('Введите заново')
    

# try:
#     a = ('see','home','file','pop') 
#     print(a.index('see'))
# except(TypeError, NameError, IndexError):
#     print('Поймал все ошибки')
# else:
#     print('Не поймал не одну ошибки!')

# try:
    
#     at = 10
#     a = 15
#     wo = 20
 
#     for e in range(-at, at):
#         print(wo / e)

#     if a > '5':
#         print(at > 5)
    
# except(TypeError,RuntimeError,IndentationError,ZeroDivisionError):
#     print('Поймал все ошибки')      

# st = []
# a = list(reversed(st))
# sls_obj = slice('0','8')
# for i in range(10):
    
    
#         lst.append(i)
#         print(а[sls_obj])


# s = []
# n = input('Введи число или end для завершения: ')

# while n != 'end':
#     if not n.isdigit():
#         print('Вы ввели не цифру введите корректно')
#         n = input('Введи число или end для завершения: ')
#         continue
#     s.append(int(n))
#     n = input('Введи число или end для завершения: ')
# else:
#     # ful = []
#     # for i in s:
#     #     ful.append(str(i))
#     # ful = ', '.join(ful) 

#     # print('your digits: ', ful)

#     print('your digits: ', ', '.join(str(i) for i in s))
#     print('summ: ', sum(s))
#     print('Arif: ', sum(s)/ len(s))
    

