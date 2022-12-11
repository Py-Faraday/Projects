# def name_file():
#     fi = input('Назовите свой файл: ')
#     f = open(f'{fi}.txt', 'a+')
#     f.close()
    
# name_file()

# def list1(a:list):
#     b = []
#     mid = len(a) //2 
#     c = a[:mid]
#     d = a[mid:]
#     d.reverse()
#     c.reverse()
#     b.extend(c)
#     b.extend(d)
#     return b
# b = ['1','5', 'age', 'name']
# print(list1(b))

# def um(x, b):
#     return x * b 
# print(um(3,8))

# def sl(s, h):
#     return s / h 
# print(sl(20,2))


# def kvadrat(x, n=2):
#     return x ** n

# print(kvadrat(15))


# def login(name, age=20):
#     return f'Ваше имя {name}, Ваш возраст {age}'
# print(login('Sam'))


# def get_number():
#     pass


# def add_contact():
#     pass


# def func(*args):
#     for i in args:
#         if i % 4 == 0:
#             return f'{i} - число четное'

# print(func(1,2,3,4,5,6,7))


# def func(**kwargs):
#     return kwargs

# print(func(key = 'value', name = 'azat'))


# def chet_nechet(x):
#     if x % 2 == 0:
#         return f'{x} - четное'
#     else:
#         return f'{x} -  не четное'

# print(chet_nechet(8))
        


# def chet_nechet(x):
#     if x % 2 == 0:
#         return f'{x} - четное'
#     return f'{x} - не четное'

# for i in range(20):
#     print(chet_nechet(i))


# def chetnoe(x):
#     if x % 2 == 0:
#         return True
#     return False


# for i in range(20):
#     if chetnoe(i):
#         print(f'{i} - четное')
#     else:
#         print(f'{i} - не четное')

# def gen_number():
#     from random import choice
#     num = '0444'
#     for _ in range(6):
#         num += choice('145790')
#     return num
# print(gen_number())

# for i in range(10):
#     print(i + 1, f'Ваш номер телефона {gen_number()}')

# def works(salary):
#     to_pay = salary * 1.7
#     if to_pay > salary:
#         print('Итог: ')
#         print('\t{0}'.format(to_pay))
        
# works(123)
# works(678)
# works(234)


