hel=input('Vvedite dannye:')
if len(hel)>=4 or len(hel)<=16:
    a = 'qwertyuiopasdfghjklzxcvbnm1234567890_'
    for hel in a:
        if hel!=a:
            print(False)
    else:
        print(True)
