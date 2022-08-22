from random import choice


variant={
    1:'камень',
    2:'ножницы',
    3:'бумага'
}

def variant_game(user_choice:int)->str:
    computer_choice=choice(list(variant))
    if user_choice==computer_choice:
        return 1,f'ничья, бот выбрал {variant[computer_choice]}'
    elif user_choice==1 and computer_choice==2 or user_choice==2 and computer_choice==3 or user_choice==3 and computer_choice==1:
        return 2,f'вы выиграли, бот выбрал {variant[computer_choice]}'
    elif user_choice==1 and computer_choice==3 or user_choice==2 and computer_choice==1 or user_choice==3 and computer_choice==2:
        return 3,f'вы проиграли, бот выбрал {variant[computer_choice]}'
    else:
        return 'выберите корректный ответ'
    


def sticker(res:int)->str:
    list_win=['static/win.tgs']
    list_nich=['static/nich.tgs']
    list_lose=['static/lose.tgs']
    if res==1:
        stk = open(choice(list_nich),'rb')
        return stk
    elif res==2:
        stk = open(choice(list_win),'rb')
        return stk
    if res==3:
        stk = open(choice(list_lose),'rb')
        return stk
while True:print(variant_game(int(input('>> 1.kamen 2.nojnicy 3.bumaga\n>>> '))))

print(sticker(variant_game(1)[0])