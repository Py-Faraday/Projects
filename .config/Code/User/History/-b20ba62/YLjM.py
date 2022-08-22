users = {
    'Admin':{
        'name':'admin',
        'phone':'996708675645',
        'balance':50000,
        'password':'12312321'
    },
    'Amina':{
        'name':'Amina',
        'phone':'996 708340678',
        'balance':500,
        'password':'12312321'

    }
}
key=None
while True:
    if key is  None:
        print('Здравствуйте уважаемый клиент')
        m=int(input('''
        1 Зарегистрироваться
        2 Авторизоваться
        3 Перевод баланса
        4 Список пользователей
        5 Информация
        6 Выход из банка
        >>>'''))
        if m == 1:
            login = input('Введите логин:')
            name = input ('Введите ваше имя:')
            phone = input('Введите ваш номер +996')
            password = input('Придумайте пароль:')
            password1 = input('Подтвердите  пароль:')
            while password == password1 and len(password)<8:
                password = input('Ваш пароль не совпадает или меньше 8 символов\<<< ')
                password1 = input('Повторите пароль')
            else:
                users.update({
                    login:{
                        'name':name,
                        'phone':phone,
                        'balance':1000,
                        'password':password
                    }
                })
                print('Регистрация успешна')
                key = login
            if m == 2:
                if key is None :
                    print('Добро пожаловать в авторизацию ')
                    login = input('Введите логин')
                    password = input('Введите пароль')
                    if login is users:
                        if password==users[login][password]:
                            print('Вы авторизовались')
                            key = login
                        else:
                            print('Не верный пароль')
                    else:
                        print('Нет такого пользователя')
                else:
                    print('Вы уже авторизованы')
                if m==3 :
                    if users is not None:
                        loginP = input('Введите имя пользователя')
                        summa = int(input('Введите сумму перевода'))
                        if loginP in users:
                            if summa <=users [key]['balance']:
                                users[key]['balance']-=summa
                                users[loginP]['balance']
                                print('перевод успешен')
                            else:
                                print('У вас не достаточно денег')
                        else:
                            print('Такого пользователя нет')
                    else:
                        print('Вы не авторизованы')
                if m ==4:
                    print(users)
                if m ==5:
                    print(f'''
                    Логин:{users["Admin"]}
                    Имя :{users["Admin"]['phone']}
                    Номер телефона:{users["Admin"]['phone']}
                    Баланс:{users["Admin"]['balance']}
                    ''')
                    if m ==6:
                        print('Приходите еще')
                        break
                    login = input('Измените имя')
                    password = input('Измените пароль')








