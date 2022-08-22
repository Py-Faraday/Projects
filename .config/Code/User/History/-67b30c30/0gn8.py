from random import randrange
while True:
    def game():
        print('''камень ножницы бумага

        Условное обозначение:
        1-Камень
        2-Ножницы
        3-Бумага
        ''')
        user=int(input('Введи ход\n'))
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
        

        if comp==user:
            print('ничья\n')
        elif comp==1 and user==2 or comp==2 and user==3 or comp ==3 and user==1:
            print(' выиграл комп \n')
        elif comp==2 and user==1 or comp==3 and user==2 or comp==1 and user==3:
            print(' вы выиграли \n')
        
    game()

