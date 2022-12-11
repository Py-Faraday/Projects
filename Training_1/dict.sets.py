# dict = {'name':'Tom',
#         'age': 12,
        
# }

# dict['123'] = 12
# dict['asd'] = 234
# dict['see'] = 675
# dict['welk'] = 766
# dict_2 = {'ask': 'wde'}
# dict.pop('123')
# dict.setdefault(7, 'seven')
# a = dict.copy()
# print(a)


# set_1 = {1,2,2,2,3,4,5,6,7}
# print(set_1)
# set_1.clear()
# print(set_1)


# set1 = {'Tom','Sara','Ria','Helen','Bob','Helly'}
# set2 =  {'Tom','Wendy','Ria','Helen','Jery','Helly'}
# set3 = set2.difference(set1)
# print(set3)11


# a = set()
# b = 10
# c = '12'
# d = True
# a.add(b) 
# a.add(c)
# a.add(d)
# print(a)

# a = {1,2,3}
# b = {4,5,6}
# a.update(b) 
# a.remove(1)
# print(a)

# dates_of_birth = {3,10,11,13,31,21,7,7,7,7,1,10,3,5,6,6}
# dates_of_birth.remove(7)
# print(dates_of_birth)

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = farm_1.intersection(farm_2)
# print(farm_3)


# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = farm_2.difference(farm_1)
# print(farm_3)


# person = {
#     'name': 'John Smith',
#      'age': 30,
#      'profession': 'Python dev'
#  }

# person['height'] = 180
# person['age'] = 40
# person3 = {'man': 'boy'}
# person.pop('age')
# print(person)


# menu = {'lagman': 135, 'plov': '120', 'borsh': 100,}
# menu2 = {'bash_barmak': 130}
# menu.update(menu2)
# menu.pop('borsh')
# menu.setdefault('drinks', ['Coca-Cola', 'Sprite','Fanta'])
# print(menu)


# person = {
#     'name': 'John Smith',
#      'age': 30,
#      'profession': 'Python dev'
#  }


# person['height'] = 180
# person['age'] = 40
# person['planet'] = 'earth'
# person2 = {'race': 'ork'}
# person.update(person2)
# person.pop('age')
# c = person.get('race')
# print(c)
# print(person)
# print(person['name'])
# print(person.items())
# print(person.keys())


# a = {}
# for _ in range(1,4):
#     person = input('введите имя:')
#     c = input('введите пароль:')
#     a[person] = c 
# print(a)    


# name ={ 'Tom': 'Python Dev', 'Eri': 'doctor', 'Gwen': 'Student','Sara': 'frontend','Mayk': 'gonshik'
# }
# for key, value in name.items():
#     print(f'здравствуйте{key} прекрасная профессия{value}')
    
    

# a = {
#      'number':[4,7,8]
#  }

# for value in a.values():
#      print(value[2])
    

# dict_1 = {}
# dict_1['one'] = 1
# print(dict_1)


# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
# 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# south_american_countries.remove('Suriname')
# print(south_american_countries)


# suitcase = ['clothes','meal','cream','towel','water'
#             ]
# suitcase.remove('water')
# print(suitcase)



# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_3 = {"dog","horse","donkey","cow"}
# farm_4 = farm_2.difference(farm_1,farm_3)
# print(farm_4)


# nums = []
# count = 0
# total = 0
# while True:
#     num = input('>>> ')
#     if num == 'end':
#         break
#     else:
#         nums.append(num)
#         count += 1
#         total += int(num)
# print('You entered: ', ', '.join(nums))
# print('Total: ', total)
# print('AVG: ', total / count)


# a = [5,8,4,3,2]
# a.sort()
# print(a)
# print(max(a))
# print(min(a))
# print(sum(a))


# dict1 = {}
# print(type(dict1))


# d = dict(short = 'dict', long = 'dictionary')
# print(d)


# dict1 = {
#      1:2,
#     'str': 'string', 
#     'bool': True,
#     'list': [1,2,3]
# }
# print(dict1)

person = {
    'name': 'Will Smith',
    'age': 30,
    'profession': 'Actor'
}
person['height'] = 180
person['age'] = 40
person['planet'] = 'Mars'
person2 = {'race': 'troll'}
person.update(person2)# обновляет словарь
# person.pop('age')# удаляет элемент по ключу
c = person.get('race') # возвращает значение по ключу
# print(person['name'])# выводит на экран значение по ключу
# print(c)
# print(person)
# person.clear()
# a = person.copy()# создает копию словаря
person.setdefault(7, 'seven')# Создает новую пару ключ:значение, но если такой ключ уже есть, ничего не произойдет
# print(person.values())# возвращает значения
# print(person.keys()) # возвращает ключи
# print(person.items())
# print(person)

# dict1 = {}
# dict1['one'] = [1,2,3]
# dict1['two'] = (4,5,6)
# print(len(dict1))


# for key in person:
#     print(key)

# for value in person.values():
#     print(value, end=', ')


# for key, value in person.items():
#     print(f'{key} = {value}')

# for key in person:
#     if key == 'name':
#         person['name'] = 'Johny Depp'
#     elif key == 'age':
#         person['age'] -= 20

# print(person)


