#a=['bael',12,34,'kanat','egida',546,23,'kiri','anna',]
#a.extend(b)

# a=[]
# b=('help','namber')
# t=(1,87)
# c=('hello',)
# d=('bema',)
# n=('rikki','gyuio')
# a.append(b)
# a.append(t)
# a.append(c)
# a.append(d)
# a.append(n)
# print(a)


# a=('nano','hello','maney')
# print(a[2])



# a=(1,2.3,'vova',True,'hello')
# print(a)




# a=('Talant','Bema','Tina','Tima','Sezim')
# b=''.join(a)
# print(b)




# a=[112,1.24,'hello','xs']
# b=['baby',46,'lili','rikki']
# a.append(a)
# a.append(b)
# print(a)

# a =['Jack','Jimmy','Jackson','Jhon','Jeckson','Jhon','Jimmy','Jeckson','Jhon','Jeckson','Jhon','Jack','Jhon','Jack']
# # a.remove('Nina')
# # print(a)



#######################
# # Лист №1:
# a = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# b =a.count('Jack')
# print(b)






# a=[]
# a.append('Aibarchyn')
# a.append(2004)
# a.append('pythot')
# print(a)


# a=list(range(1,100,2))
# print(a)



# a=list(range(16,100,20))
# a.reverse()
# print(a)



# print([i for i in 'hello world'.split])





# text = 'hello world'
# s = text.split()
# print(s)





Endless Key, [21/7/22 22:49]
[В ответ на Nikiman]
Ууее 😂

kiri, [22/7/22 09:33]
добое утро

kiri, [22/7/22 09:35]
faster

kiri, [22/7/22 10:56]
#######################
# # Лист №1:
# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]

# Задача 1
# Есть список:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#



a = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]






start = int(input(
    'Введите старт: '
))

stop = int(input(
    'Введите stop: '
))

step = int(input(
    'Введите step: '
))

if step <= 0:
    print('шак не может быть меньше 1')

else:
    lst = list(range(start, stop+1, step))
    print(lst)