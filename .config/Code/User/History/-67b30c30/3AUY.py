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
        print('Твой выбор Камень')
    elif user==2:
        print('Твой выбор ножницы')
    elif user==3:
        print('Твой выбор Бумага')
    else:
        print('Не правильное значение')
