# def add(x, f=8):
#     return x + f 
    

# print(add(3))


# def stri(c):
#     a = ('medetova egida')
#     for 




# def chetnoe(x):
#     if x % 2 ==0:
#         return True
#     return False

# # print(chetnoe(9))


# for i in range(1,3):
#     if chetnoe(i):
#         print(i, 'четное') 
#     else:
#         print(i, 'нечетное')



# def count_vowels(text: str): 
#     vowels=('у' ,'е', 'о', 'а', 'и' ,'ы')
#     res = 0 
#     for letter in text: 
#         if letter.lower() in vowels: 
#             res += 1
#     return res 
# print(count_vowels('урщь'))



from random import choice
from os import system
from string import ascii_letters

# def f(x):
#     for i in range(x):
#         fn = ''
#         while len(fn) < 6:
#             fn += choice(ascii_letters)
#         print(f'touch {fn}.txt')   
            
# f(5)
        

# def polindrom(x):
#     if x != x[::-1]:
#         return False  
#     else:
#         return True

# print(polindrom('lol'))

# a = [56,9,9,45,345,89] 
# def sorts(x):
#     x.sort()
#     text = ''
#     for i in x:
#         text += str(i)
#         text += ' '
#     return text
# print(sorts(a))


# x = 'hello'
# print(x)
# print(x[::-1])


# def hello(name,muvi):
#     print(f'привет {name}')
#     print(f'отличный фильм {muvi}')

# hello ('искендер','атака титанов')
# hello ('баель','актан акылый') 
    

# def name(text):
#     text = f'<h1> {text} </h1>'
#     return text
# print(name('brazzers'))


# def name(text):
#     for i in text:
#         try:
#             int(i)
#         except:
#             return False
#     return True
# print(name('123'))


from os import system
# # os.system('ls > files.txt')
# # l1 = []
# # with open('files.txt', 'r') as f:
# #     l = f.read().split()
# #     for i in l:
# #         if i.endswith('.txt'):
# #             os.system(f'rm -rf {i}')

# a = input('>>')
# def func(l):
#     from os import system
#     os.system('ls > files.txt')
#     l1 = []
#     with open(f'files.txt', 'r') as f:
#         files_names = f.read().split()
#         for i in files_names:
#             if i.endswith(l):
#                 os.system(f'rm -rf {i}')
# func(a)







