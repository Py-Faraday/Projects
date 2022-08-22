from random import choice

varianat = {
    1: 'камень',
    2: "ножницы",
    3: "бумага"
}

def varianat_game(user_choice: int) -> str:
    coumputer_choice = choice(list(varianat))
    if user_choice == coumputer_choice:
        return f"Ничья, Бот выбрал {varianat[coumputer_choice]}"
    elif user_choice == 1 and coumputer_choice == 2 \
        or user_choice == 2 and coumputer_choice == 3 \
            or user_choice == 3 and coumputer_choice == 1:
        return f"Вы выйграли, Бот выбрал {varianat[coumputer_choice]}"
    
    elif user_choice == 1 and coumputer_choice == 3 \
        or user_choice == 2 and coumputer_choice == 1 \
            or user_choice == 3 and coumputer_choice == 2:
        return f"Вы проиграли, Бот выбрал {varianat[coumputer_choice]}"

    else:
        return 'Выберите корректный ответ'


def stiker(result:int)->str:
    sts=varianat_game()
    list_win=['static/win.tgs']
    list_nowin=['static/nowin.tgs']
    list_nichia=['static/nichia.tgs']
    sts=open(choice(list_win),'rb')
    if sts==1:
        
        sts=open(choice(list_win),'rb')
        return sts
    if sts==2:
        sts=open(choice(list_nowin),'rb')
        return  sts
    if sts==3:
        sts=open (choice(list_nichia),'rb')

    



#while True:(varianat_game(int(input('>>> 1.kamen 2.nojnisa 3.bumaga\n>>>>>'))))