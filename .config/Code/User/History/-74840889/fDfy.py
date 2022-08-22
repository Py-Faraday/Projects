# a =[1,2,3,3,4,5,6,7,8,9,0]
# b=[1,2,3,3,4,5,6,9,90,6,7,8,9,0]
# def my_len(maasiv):
#     s = 0 
#     for i in maasiv:
#         s +=1
#         return s

# print(my_len(a))
# print(my_len(b))


# def my_sum(a,b,n):
#     return a +b +n
# a =my_sum(6,7,90)
# print(a)


# print1 = print
 
 
# def print(*a):
#     for i in a:
#         print1(i.upper(), end=' ')




# list=['name','age','1','19']


# list.reverse()
# print(list)


# a = 0
# b = 1
# n = 10 
# i = 0
# while i < n - 2:
#     z = a + b
#     a = b
#     b = z
#     i = i + 1
#     print(z)
# print(b)



f = [0,1]
[f.append(f[-2]+f[-1])for i in range(10)]
print(f)


# list=['name','age','1','19']
# def my_reverse(list1):
#     mid = len(list1)//2
#     a=list1[:mid]
#     b =list1[mid:]
#     a.reverse()
#     b.reverse()
#     return a+b
# print(my_reverse)
# a = [1,2,3,4,5,6]
# print(my_reverse(a))