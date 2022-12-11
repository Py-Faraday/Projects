# class Product:
#     name = 'iphone' 
#     model = '13pro'
#     price = '100000'
#     idt = 123
    
# p = Product()
# p.price = 120000
# print(p.price)


# class Dog:
#     name = 'Tom'
#     brend = 'buldog'
#     color = 'black'
#     age = 4
    
#     def back_back(self):
#         return f'Пес по кличке {self.name} гавкнул'
    
#     def run(self):
#         return f'Пес по кличке {self.name} побежал'

# dog1 = Dog()
# print(dog1.back_back())
# print(dog1.run())
# print(f'{dog1.name} {dog1.age} годика')


# class Car:
#     name = 'Bmw'
#     model = 'model12'
#     color = 'black'
#     age = 5

#     def run(self):
#         return f'{self.name} машина начала ехать'

#     def open_door(self):
#         return f'У {self.name} открылась дверь'

# car1 = Car()
# car1 = Car()

# car1.model = 'model6789'

# print(car1.run())
# print(car1.open_door())


# class Car:
#     title = 'honda'
#     def __init__(self,model: str,body: str,color: str):
#         self.model = model
#         self.body = body 
#         self.color = color
        
#     def info(self):
#         return f'{self.title} {self.body} {self.color}'
        
# car1 = Car(input('Enter the model: '),'Sentan', 'black')
# print(car1.info())


# Task 1 

# class Acer:
#     def __init__(self,processor: str,memory: int,video_carta:int ,disk:str ,motherboard:str ,screen_size:int, model: str) -> None:
#         self.processor = processor
#         self.memory = memory 
#         self.video_carta = video_carta
#         self.disk = disk
#         self.motherboard = motherboard
#         self.screen_size = screen_size
#         self.model = model


# acer1 = Acer('CDU',123, 34, 'HDD', 'MSI', 234, 'QWE12')

# print(acer1.__dict__)


# Task 2 

# colors = { "black": { "category": "hue", "type": "primary", "code": { "rgba": [255,255,255,1], "hex": "#000" } }, "white": { "category": "value", "code": 
#         { "rgba": [0,0,0,1], "hex": "#FFF" } }, "red": { "category": "hue", "type": "primary", "code": { "rgba": [255,0,0,1], "hex": "#FF0" } }, "blue": { "category": "hue", "type": "primary", "code": { "rgba": [0,0,255,1], "hex": "#00F" } }, 
#         "yellow": { "category": "hue", "type": "primary", "code": { "rgba": [255,255,0,1], "hex": "#FF0" } }, "green": { "category": "hue", "type": "secondary", "code": { "rgba": [0,255,0,1], "hex": "#0F0" } } }
    

# class Classroom:
#     def __init__(self,color: str,integer:int, string:str):
#         self.color = color
#         self.integer = integer
#         self.string = string 
# my 
    
        



# colors = {
# "black": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,255,255,1],
# "hex": "#000"
# }
# },
# "white": {
# "category": "value",
# "code": {
# "rgba": [0,0,0,1],
# "hex": "#FFF"
# }
# },
# "red": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,0,0,1],
# "hex": "#FF0"
# }
# },
# "blue": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [0,0,255,1],
# "hex": "#00F"
# }
# },
# "yellow": {
# "category": "hue",
# "type": "primary",
# "code": {
# "rgba": [255,255,0,1],
# "hex": "#FF0"
# }
# },
# "green": {
# "category": "hue",
# "type": "secondary",
# "code": {
# "rgba": [0,255,0,1],
# "hex": "#0F0"
# }
# }
# }


# a = []
# for key,value in colors.items():
#     a.append(key)
#     for j,k in value.items():
#         a.append(j)
#         try:
#             for key2, value2 in k.items():
#                 a.append(key2)
#         except:
#             pass    
            

# print(a)


# Task 3 

# class Data:
#     data = { "markers": [ { "name": "Rixos The Palm Dubai", "position": [25.1212, 55.1535], }, 
#                             { "name": "Shangri-La Hotel", "location": [25.2084, 55.2719] }, 
#                             { "name": "Grand Hyatt", "location": [25.2285, 55.3273] } ] }
#     data2 = []

#     for value in data.values():
#         for j,z in data.items():
#             if j == 'name':
#                 data2.append(data)
        
        

