# l = [23,34,12,90]

# def my_lists(list1):
#     list2 = []
#     a = list1[:2]
#     b = list1[2:]
#     a.reverse()
#     b.reverse()
#     a.append(list2)
#     b.append(list2)
#     return list2
# print(my_lists())





# a = 0
# b = 1
# n = 10 
# i = 0
# while i < n - 2:
#     z = a + b
#     a = b
#     b = z
#     i = i + 1
#     print(z)
# print(b)


# def number(x,w):
#     return x + w
    
# def number2(x,w):
#     return x - w 

# def number3(x,w):
#     print(number(x,w))
#     print(number2(x, w))
    
# number3(5, 6)
# number3(76, 54)


# def print_asan():
#     print('hello')
#     print('world')
#     print('asan')
    
# print_asan()
# print_asan()
# print_asan()

# print(print_asan())


# a = [1,2,4,5,6,7,64,3,3,2,4,5,6,6]
# b = [1,2,4,2,3,6,5,6,7,64,3,3,2,4,5,6,6]


# def my_len():
#     s = 0
#     for i in a:
#         s += 1
#     print(s)
# def my_len(maasiv):
#         s = 0
#         for i in maasiv:
#             s += 1
#         return s

    



# print(len(a))
# print(my_len(b))

    
    
# name = {1 : '12',
#         2: '13',
#         3 : '56',
#         4 : '45'}
# def my_name():



# def gen_number():
#     from random import choice 
#     num = '0444'
#     for i in range(6):
#         num += choice('145790')
        
#     return num
    


# text = f'Ваш номер телефона {gen_number()}'
# print(text)


# def kvadrat(x, n = 3):
#     return x ** n 
# print(kvadrat(2, ))


# def add(x, b=3):
#     return x + b 
    

# print(add(3))


# def substract(x, b=3):
#     return x - b 
    

# print(substract(3))


# def multiply(x, b=3):
#     return x * b 
    

# print(multiply(3))


# def divide(x, b=3):
#     return x / b 
    

# print(divide(3))




# a = [1,3,46,79,'rei','sara']
# def my_len(i):
#     s = 0
#     for i in a:
#         s += 1
#     return s
    




# print(my_len(a))


# dic = {1 : '23',
#        2 : '89',
#        3 : '34'
# }
# dic2 = {4 : '90',
#         5 : '78',
#         6 : '67'    
# }


# def my_dictionary():
#     dic.update(dic2)
#     return dic

# print(my_dictionary())



# def a():
#     a = input('ЧТО БУДЕШЬ ')
#     b = input('что пить ')
#     f = open(f'предпочтение.txt','a+')
#     f.write(f'{a},{b}\n')
#     f.close()
# a()


# def x():
#     x = input('Названия файла:')
#     f = open(f'{x}.py', 'a+')
#     f.close()
# x()

# def function(main_page):
#     def function_2(nested):
#         return main_page + nested
#     return function_2
    
# x = function('Я главная функция')
# print(x ('\nЯ вложеная функция'))


# def key():
#     tu = {1 : '90',
#            2 : '34',
#            3 : '56',        
#     }
#     return tuple(tu.keys()),tu.values()

# print(key())



# a = []
# for i in range(2,100):
#     k = 0 
#     for j in range(2 , i):
#         if i % j == 0:
#             k +=1
#     if k == 0:
#         a.append(i)
# print(a)


        
   

# def func(*args):
#     for i in args:
#         if i % 2 ==0:
#             return i
#     print('hello')

# print(func(1,3,4,5,6,7,87,4))



# def func(**kwargs):
#     return kwargs

# print(func(name='aktan', age=17))


# def key():
#     tu = {1 : '90',
#            2 : '34',
#            3 : '56',        
#     }
#     return list(tu.keys()),tu.values()

# print(key())



# def num():
#     a = int(input('Вводите любое число:'))
#     x = []
#     n = ''
      






# def i():
#     name = input('Введите свое имя:')
#     wages = int(input('Введите свою зарплату:'))





