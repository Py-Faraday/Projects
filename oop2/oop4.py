# class Car:
#     def __init__(self,names:str,model:str,color:str):
#         self.names = names 
#         self.model = model 
#         self.color = color 
        
# class Md(Car):
#     def run(self):
#         return f'машинка начала ездить'

# car1 = Car('QWE', 'TYU', 'white')
# mers = Md('scrabes','MSS','black')

# print(mers.run())
# print(car1.run())

# class Person:
#     def __init__(self,name: str,surname: str,age: int):
#         self.name = name 
#         self.surname = surname 
#         self.age = age 

# class Doctor:
        
#     def beal(self):
#         return f'{self.name} решил вас лечить'
    
    
#     def qwe(self):
#         return f'{self.name} решил покушать'
  
    
# class Nurse(Doctor):
#     def clizma(self):
#         return f'Получай клизму'
    
#     def inject(self):
#         return f'{self.name} ставит укол'
    
# class Medbrothers(Nurse):
#     pass


# d = Doctor('Tom', 'Peteson', 34)
# n = Nurse('Sara',"Petersan",24)
# m = Medbrothers('Fred','Frenkson',48)
    
# print(d.beal())
# print(n.inject())
# print(m.qwe())



# class Fireman(Person):
#     def tushit(self):
#         return f'{self.name} решил вас потушить'
    
# f = Fireman('Max', 'Peterson', 34)
# print(f.tushit())


# Task 1
# class Factory:
#     def __init__(self,engine:str, bridge: str):
#         self.engine = engine
#         self.bridge = bridge

#     def engine1(self):
#         return f'Двигатель создан'
    
#     def bridge1(self):
#         return f'Ходовая часть создана'
    
    
# f = Factory('Двигатель', 'Ходовая')

# # print(f.bridge1())
# # print(f.engine1())

# class Toyota(Factory):
#     def wheelse(self):
#         return f'Колёса готовы'
    
#     def window(self):
#         return f'Стёкла готовы'

# t = Toyota('qwer', 'rtyu')
# print(list(t.wheelse()))
# print(list(t.window()))


# Task 2

# class Zoo:
#     def __init__(self):
#          self.animal_1 = 'Тигр'
#          self.animal_2 = 'Бегемот'
#          self.animal_3 = 'Жираф'
#          self.animal_4 = [self.animal_2, self.animal_3]

# z = Zoo()
# z.animal_4[1] = 'Змея'
# print(z.animal_4)

# z.animal_1 = "Лев"
# print(z.animal_1)


# Task 3 
user_data = {
  "id": 1,
  "first_name": "Humphrey",
  "last_name": "Wilcox",
  "email": "hwilcox0@odnoklassniki.ru",
  "gender": "Male",
  "ip_address": "80.232.175.95"
}, {
  "id": 2,
  "first_name": "Erhard",
  "last_name": "Byart",
  "email": "ebyart1@addthis.com",
  "gender": "Male",
  "ip_address": "125.7.237.155"
}, {
  "id": 3,
  "first_name": "Brok",
  "last_name": "Leiden",
  "email": "bleiden2@usnews.com",
  "gender": "Male",
  "ip_address": "108.201.248.102"
}, {
  "id": 4,
  "first_name": "Gradeigh",
  "last_name": "Spreckley",
  "email": "gspreckley3@marriott.com",
  "gender": "Male",
  "ip_address": "90.169.195.245"
}, {
  "id": 5,
  "first_name": "Trueman",
  "last_name": "McArd",
  "email": "tmcard4@cargocollective.com",
  "gender": "Male",
  "ip_address": "249.26.239.198"
}, {
  "id": 6,
  "first_name": "Giacobo",
  "last_name": "Rishworth",
  "email": "grishworth5@merriam-webster.com",
  "gender": "Male",
  "ip_address": "156.104.68.219"
}, {
  "id": 7,
  "first_name": "Marcia",
  "last_name": "Burney",
  "email": "mburney6@gmpg.org",
  "gender": "Female",
  "ip_address": "52.104.185.232"
}, {
  "id": 8,
  "first_name": "Court",
  "last_name": "Haysar",
  "email": "chaysar7@eepurl.com",
  "gender": "Hidden",
  "ip_address": "60.138.180.175"
}, {
  "id": 9,
  "first_name": "Penn",
  "last_name": "Slatten",
  "email": "pslatten8@narod.ru",
  "gender": "Male",
  "ip_address": "216.91.212.228"
}, {
  "id": 10,
  "first_name": "Rayna",
  "last_name": "Jacobsson",
  "email": "rjacobsson9@4shared.com",
  "gender": "Female",
  "ip_address": "158.81.126.17"
}, {
  "id": 11,
  "first_name": "Elissa",
  "last_name": "Milch",
  "email": "emilcha@ucoz.ru",
  "gender": "Female",
  "ip_address": "160.46.17.104"
}, {
  "id": 12,
  "first_name": "Cissiee",
  "last_name": "Dever",
  "email": "cdeverb@dailymail.co.uk",
  "gender": "Hidden",
  "ip_address": "198.12.171.92"
}, {
  "id": 13,
  "first_name": "Lorie",
  "last_name": "Cavozzi",
  "email": "lcavozzic@apache.org",
  "gender": "Female",
  "ip_address": "252.228.114.151"
}, {
  "id": 14,
  "first_name": "Shelton",
  "last_name": "Pipe",
  "email": "spiped@opera.com",
  "gender": "Male",
  "ip_address": "217.193.203.141"
}, {
  "id": 15,
  "first_name": "Cordell",
  "last_name": "Hrinchenko",
  "email": "chrinchenkoe@ovh.net",
  "gender": "Transgender",
  "ip_address": "147.76.167.191"
}, {
  "id": 16,
  "first_name": "Dyanna",
  "last_name": "Sizzey",
  "email": "dsizzeyf@xing.com",
  "gender": "Female",
  "ip_address": "8.177.20.12"
}, {
  "id": 17,
  "first_name": "Felice",
  "last_name": "Floyed",
  "email": "ffloyedg@instagram.com",
  "gender": "Male",
  "ip_address": "4.150.254.58"
}, {
  "id": 18,
  "first_name": "Arel",
  "last_name": "Donoher",
  "email": "adonoherh@youtu.be",
  "gender": "Male",
  "ip_address": "186.214.243.230"
}, {
  "id": 19,
  "first_name": "Kristoffer",
  "last_name": "Carvill",
  "email": "kcarvilli@xinhuanet.com",
  "gender": "Male",
  "ip_address": "58.204.72.103"
}, {
  "id": 20,
  "first_name": "Norbie",
  "last_name": "Oleksinski",
  "email": "noleksinskij@free.fr",
  "gender": "Male",
  "ip_address": "242.192.49.216"
}

