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
        if i <0:
            b+=i
    return(a,b)
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

          