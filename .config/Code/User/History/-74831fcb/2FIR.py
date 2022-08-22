from random import choice
from os import system
from string import ascii_letters 

def my_random(x):
    for i in range(x):
        file_name=''
        while len (file_name)<6:
            file_name +=choice(ascii_letters)

        system(f'touch {file_name}.txt')
my_random(4)
    

    


