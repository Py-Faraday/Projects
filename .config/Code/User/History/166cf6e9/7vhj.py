hel=input('Vvedite dannye:')
if len(hel)>=4 or len(hel)<=16:
    for i in hel:
        if i != int and str:
            print(False)
    else:
        print(True)
