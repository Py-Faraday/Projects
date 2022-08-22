import os

sayt =input()
if 'https//' in sayt:
    os.sistem('start '+sayt)
    print('if')
elif 'www,'in sayt:
    sayt = 'https://'+ sayt
    os.sistem('start '+ sayt)
    print('elif')
else:
    sayt = ('https://www ,'+ sayt)
    os.sistem('start '+sayt)
    print('else')    
