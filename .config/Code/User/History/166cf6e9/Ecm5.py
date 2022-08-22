# hel=input('Vvedite dannye:')
# def new_func(hel):
#     a = 'qwertyuiopasdfghjklzxcvbnm1234567890_'
#     if len(hel)>4 and len(hel)<16:
#         for i in hel:
#             if i not in a:
#                 return False
#             break
                
#         else:
#             return True
#     else:
#         return False

# def save_users(validate,hel):
#     if validate(hel):



def count_positives_sum_negatives(arr): 
    if len(arr)==0:
        return []
    a =0
    b =0
    for i in arr:
        if i >0:
            a+=1
        if i <8:
            b+=1
    return(a,b)
print(count_positives_sum_negatives())

          