from random import randrange
def game():
    print('''камень ножницы бумага

    Условное обозначение:
    1-Камень
    2-Ножницы
    3-Бумага
    ''')
    user=int(input('Введи ход'))
    print(user)
    if user==1:
        print('Твой выбор Камень\n')
    elif user==2:
        print('Твой выбор ножницы\n')
    elif user==3:
        print('Твой выбор Бумага\n')
    else:
        print('Не правильное значение')
    comp=randrange(3)+1
    if comp==1:
        print('выбор компа Камень\n')
    elif user==2:
        print('выбор компа ножницы\n')
    elif user==3:
        print('выбор компа Бумага\n')
    else:
        print('Не правильное значение')

    # if comp==user:
    #         print('ничья\n')
    #     elif user==2:
    #         print(' комп \n')
    #     elif user==3:
    #         print(' компа Бумага\n')
    #     else:
    #         print('Не правильное значение')

