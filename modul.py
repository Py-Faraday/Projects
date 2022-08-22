# import random 
# print(random.random())


# import random 
# from random import random,randint
# print(randint(1,10))


import random 
from random import random, randint, randrange, choice,shuffle
from time import sleep 
from tracemalloc import start 
# print(randrange(0,100,3))


name = ['rey','tom','sara','gery']


# print(choice(name))
# for u in name:
#     print(u)
#     sleep()
    
    
from datetime import datetime, time
# print(datetime.today().strftime('%d-%m-%y %H:%M:%S'))
# now = datetime.now ()
# print(now)
# time1 = time(4,3,23)
# time2 = time(4,3,0)

# print(time1, time2)


import os
# os.mkdir('World')
# os.system('rm -rf World')
# os.system('clear')

from string import ascii_letters 

# print(ascii_letters)

# while True:
#     password = ''
#     while len(password) < 8:
#         l = choice(ascii_letters)
#         password += l
    
#     print(password)
#     sleep(0.9)
#     os.system('clear')
    

# password = 'QWE'
# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# count = 0
# new_password=''
# while new_password !=password:
#     new_password=''
#     while len (new_password)<3:
#         new_password +=choice(letters)
#     count+=1
#     print(new_password)
#     print(count)



# import os 
# import random as r
# try:
#     import nomodule
# except ImportError:
#     print('Нету такого модуля')
# print(r.random())

