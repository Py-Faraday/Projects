hel=input('Vvedite dannye:')
def new_func(hel):
    a = 'qwertyuiopasdfghjklzxcvbnm1234567890_'
    if len(hel)>4 and len(hel)<16:
        
        for i in hel:
            if i not in a:
                return (False)
            break
                
        else:
            return (True)
    else:
        return(False)
