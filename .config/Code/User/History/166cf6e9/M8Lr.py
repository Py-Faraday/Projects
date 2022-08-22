hel=input('Vvedite dannye:')
if len(hel)>4 and len(hel)<16:
    a = 'qwertyuiopasdfghjklzxcvbnm1234567890_'
    for i in hel:
        if i is not a:
            print (False)
        break
    else:
        print(True)
else:
    print(False)
