# a = [1,2 ,100]
# i = 



# a = list(range(1,10))
# print(a)


# a = list(range(5, 50, 3))
# print(a)


# for i in range(5, 50, 3):
#     if i != 35:
#         print(i)


# for hour in range(24):
#         for minut in range(60):
#             print(f'{hour}часов {minut}минут')
    
    
# a =(1,3,5,7,3,7,9,12,34,46)
# s = set(a)    

# if len(a) != len(s) :
#     t = len(a) - len(s)
#     print('они повторяются')   
    
# else:
#     print('они уникальны')


# nums = [1,2,3,4,4,5,5,6,6,7,]
# s = set(nums)
# nums_t = []
# for i in s:
#      if nums.count(i) > 1:
#          a = (i, nums.count(i))
#          nums_t.append(a)
#          print(nums_t)


# nums_t = [(i, nums.count(i)) for i in set(nums) if nums.count(i) > 1]
# print(nums_t)   


# a = {1:1,
#       2:2,
#       'lius':{
#       'see':5,
#       '1':3,
#       '9':9
#       }
#  }

# print(a['lius']['see'])

# s = {}
# for key, value in a['lius'].items():
#     if key == 'see':
#         s[key] = value
        
        
# print(s)

# users = {224552345678:{
#         'name':'egida',
#          'b_year':'2009',
#          'gender':'animeshnik',
#          'last_name': 'qwert',
#          'ID': 'EG1234'
#         }
# }
# users[234567654323] = {'name': 'alina',
#          'b_year':'2000',
#          'gender':'girl',
#          'last_name':'Alina',
#          'ID': 'AG3455'
    
# }

# name = input('Введите имя:')
# b_year = input('Введите год рождения:')
# gender = input('Введите гендер')
# last_name = input('Введите последнее имя:')
# id = input('Введите айди:')

# users[234567654323] = {'name': name,
#          'b_year':b_year,
#           'gender':gender,
#           'last_name':last_name,
#           'ID': id}



# print(users)


# a = list(range(5, 50, 3))
# print(a)


# import time

# for hour in range(24):
#     for minut in range(60):
#          for second in range(60):
#              print(f'{hour}:{minut}: {second}')
#              time.sleep(1)
 

# nums = [1,2,3,3,3,34,56,7,8,9,0,87,5,4,3,35,5,35,54,35,634,6,4,6,3]

# nums_t = []
# for i in set(nums):
#      if nums.count(i) > 1:
#          nums_t.append((i, nums.count(i)))
# print(nums_t)


# nums = [1,2,3,3,3,34,56,7,8,9,0,87,5,4,3,35,5,35,54,35,634,6,4,6,3]
# nums_t = [(i, nums.count(i)) for i in set(nums) if nums.count(i) > 1]

# print(nums_t)


# a = [(3, 2), (4, 2), (35, 2)]
# s = set(a)

# if len(a) != len(s):
#      t = len(a) - len(s)
#      print('Значения повторяются', t)

# else:
#      print('они уникальны')

# print(a)
# print(s)


# a = {1,1,1,1,1,1,1,1,1,1,1,1,1,1}

# print(a)


# a = {
#      ''
#  }


# a = 'они сказали "УРАА"  !!!'

# a = [1, 4, [3,43,5,7], 8]
# print(a[2])


# a = {
#       1:1,
#       (2,4):89,
#       'lius': {
#           "tree":3,
#           '4':43,
#           '5':5,
#           "7":7
#           }
#   }

# print(a['lius'])


# s = {}
# for key, value in a['lius'].items():
#      if key == 'tree':
#          s[key] = value
    
# print(s)



# a = 585.9
# print(int(a))


# users = {
#      '2109128304301812': {
#          'name': 'Asan',
#          'last_name': 'Usenov',
#          'b_year': 2000,
#          'gender': 'M',
#          'status': False,
#          'ID': 'AK4724'
#      },
#      '2109128304301232': {
#          'name': 'Aktan',
#          'last_name': 'Asanov',
#          'b_year': 2022,
#          'gender': 'M',
#          'status': False,
#          'ID': 'AK4723'
#      }
#  }

# users['21206201400345'] = {
#      'name': 'Indira',
#      'last_name': 'Ruslanova',
#      'b_year': 1999,
#      'gender': 'F',
#      'status': True,
#      'ID': 'I324324'
#  }

# inn = input('Введите ИНН: ')
# name = input('Введите name : ')
# last_name = input('Введите last_name : ')
# b_year = input('Введите b_year : ')
# gender = input('Введите gender : ')
# status = input('Введите status : ')
# id = input('Введите ID : ')

# users[inn] = {
#     'name': name,
#     'last_name': last_name,
#     'b_year': b_year,
#     'gender': gender,
#     'status': status,
#     'ID': id
# }





# print(users)
# print(users['2109128304301232'])




    


