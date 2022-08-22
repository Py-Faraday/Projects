# if True:
#     print('hello')


# print(5/0)
# try:
#     a = int(input('vvedite sivru:'))
#     b = int(input('vvedite sifru:'))

#     print(a/b)
# except ZeroDivisionError:
#     print('na 0 ne delitsa!')
# except NameError:
#     print('net takogo')

# except ValueError:
#     print('')

# while True:
#     try:
#         a = int(input('vvedite sivru:')) 
#         b = int(input('vvedite sifru:'))
#         print(a/b)
#     except ZeroDivisionError:
#         print('na 0 ne delitsa!')
#     except NameError:
#         print('net takogo')



# try:
#     a = int(input('vvedite sivru:')) 
#     b = int(input('vvedite sifru:'))
#     print(a/b)
# except(ZeroDivisionError,NameError,ValueError):
#     print('poimal vse oshinki!')
# else:
#     print('ne poimal ni odnu oshibku')
# finally:
#     print('FINALLY')



# try:
#     print('vgl'/5)
# except TypeError as e:
#     print('kod vrub iz oshibki {e}' )

# a = [True,True,True]
# print(all(a))


# a = [1,2,3,4,5,67,8,9,8]
# # b = []
# for i in a:
#     if i%2==0:
#         b.append(True)
# else:
#         b.append(False)
# print(min(a))
# print(max(a))
# b =reversed(a)
# print(list(b))
# while True:
#     eval(input('>>>'))
# print(slice(a,5,2))
# a = 10/3
# print(round(a,1))








############  1
# values = ['adam', '74955645', 787, ['set','dict'], {'set is set'}]
# b = []
# for i in values:
#     try:
#         set(i)
#         b.append(True)
#     except :
#         b.append(False)
# print(all(b))

############   2  
        
# try:
#     set1=set()
#     for i in range(5):
#         a = int (input('Введите число:'))
#         set1.add(a)
# except ValueError as t:
#     print(f'У вас ошибка {t}')
# except NameError as t:
#     print(f'У вас ошибка {t}')
# print(min(set1))
    

##########  3 
    


# try:
#     while True:
#     python = [print,range,len,str,int,float,list,tuple,dict,set,bool,]
# a = int(input('Ввод функции:'))
# for i in python:
#     if i==python:
#         print('Исполнение!')
# else:
#         print('Такой функции нет!')
# print(python)



############ 3

# while True:
#     a = input('Введите функцию:')

#     print('Исполнение!')
#     try:
#         eval(a)
#     except:
#         print('Нет такой функции')

############# 4 

values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
b = []
for i in values:
    try:
        set(i)
        b.append(0,1)
    except:
        b.append(4,5)   
    print(i)











# Code #1:

# at = 10
# in = 15
# wo = 20

# for e in range(-at, at):
# print(wo / e)
# if at > '5':
# print("at > 5)


# Code #2:
# lst = []
# for i in renge(10):
# lst.apend(i)

# a = list(revesed(lst))
# sls_obj = slice('0','8')
# print(а[sls_obj])


# Code #3:
# a = (0)
# b = (1,)
# numbers = []
# while b > a:
# numbers += b
# b += 1


