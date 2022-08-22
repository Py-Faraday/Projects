# sum_arg = lambda a:a**2
# print(sum_arg(2))


# a = (lambda a,b:a +b)(5,6)
# print(a)


# a =[1 ,2 ,4 ,5 ,6 ,7 ,8]
# for i in range(len(a)):
#     a[i]=(lambda a:a**2)(a[i])
# a[1]=5

# s = map((lambda x:x**3),a)
# print(list(s))

# 100
# # 30
# s = (lambda x,n:n*100/x)(150,75)
# print(s)



# def hell(x):
#     if x != 0:
#         print(x)
#         x -= 1
#         hell(x)
#     else:
#         print('finish')
# hell(6)

# def hel(x):
#     while x:
#         if x !=0:
#             print(x)
#             x -=1
#     else:
#             print('finish')
# hel(5)

# def greet(name):
#     return f'Hello, <name> how are you doing today?'
from tkinter.messagebox import NO, YES


def bool_to_word(boolean):
    if True==boolean:
        print(YES)
    if False==boolean:
        print(NO)
bool_to_word()
    
    
