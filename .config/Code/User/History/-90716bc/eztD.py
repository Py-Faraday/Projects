import random
from random import random,randrange,choice,shuffle
import time
from time import time

from datetime import datetime
from secrets import choice

# print(datetime.today().strftime('%d-%m-%y %H:%M:%S'))
# a = ['rikki','aika','beks','popi','bael','mars','baizak']
# for i in a:
#     print(i)
#     sleep(1)
# # shuffle(a)
# shuffle(a)
# print(a)
# now=datetime.now()
# print(now)


# timeobj = time(8,1,50)
# timeobj2 = time(8,1,50)
# print(timeobj,timeobj2)
# start = datetime.now()
# for i in a:
#     print(i)
# end = datetime.now()
# print(end-start)
# import os

# os.system('clear')
# os .system('mkdir hello')
# os.system('cd hello')



password = 'QWE'
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
while True:
    password=""
    while len(letters)==3:
        l = choice(letters)
        password +=l
        print(password==letters)



      
