# sum_arg = lambda a:a**2
# print(sum_arg(2))


# a = (lambda a,b:a +b)(5,6)
# print(a)


a =[1 ,2 ,4 ,5 ,6 ,7 ,8]
# for i in range(len(a)):
#     a[i]=(lambda a:a**2)(a[i])
# a[1]=5
print(list(map((lambda x:x**2),a)))
