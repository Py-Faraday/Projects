# class Rectangle:
#     def __init__(self, x = int, y = int):
#         self.x = x 
#         self.y = y 
        
#     def _get_rectangle(self):
#         return self.x * self.y 
    
#     def __str__(self) -> str:
#         return f'Прямоугольник {self.x} * {self.y} = {self.get_rectangle()}'
    
# class Sqware:
#     def __init__(self, x = int, y = int):
#         self.x = x 
#         self.y = y 
        
#     def _get_eq(self):
#         return self.x * self.y 
    
#     def __str__(self) -> str:
#         return f'Квадрат {self.x ** 2} = {self.get_eq()}'
    
    
# class Circly:
#     def __init__(self, r = int, p = int):
#         self.r = r 
#         self.p = p 
        
#     def _get_cir(self):
#         from math import pi
#         return pi * self.r ** 2 
    
#     def __str__(self) -> str:
#         from math import pi
#         return f'Круг {pi * self.r ** 2} = {self.get_cir()}'
    
# r1 = Rectangle(3,6)
# r2 = Rectangle(78,9)

# s1 = Sqware(56,23)
# s2 = Sqware(67,23)

# c1 = Circly(45,12)
# c2 = Circly(67,34)

# list_ex = [r1,s1,c1]
# for i in list_ex:
#     if type(i) == Rectangle:
#         print(i._get_rectangle())
#     elif type(i) == Sqware:
#         print(i._get_eq())
#     elif type(i) == Circly:
#         print(i._get_cir())
# class Summ:
#     a = 56 
#     v = 45

# @property
# def sum(self):
#     return  self.a * self.v 
    
# def um(self):
#     u = int(input('Введите число: '))
#     return u * self.sum

# s = Summ()
# print(s.um())



# class Tomato:
#     states = {'''
#         1.Absent
#         2.Flowering
#         3.Green 
#         4.Red 
#     '''}
    
#     def __init__(self, index = 0) -> None:
#         self.index = index
        
#     def grow(self):
#         self.index += 1 
#         return f'Помидор созрел до уровня{self.index}'
    
#     def is_ripe(self):
#         self.grow()
        # return f'{self.index}'
    
# class Tomatobush:
#     def __init__(self, tomatoes = Tomato()) -> None:
#         self.tomatoes = tomatoes
        
#     def grow_all(self):
#         for i in self.tomatoes:
#             i.grow()
#             print(f'Помидоры созрели {self.states[self.index]}') 
            
#     def all_are_ripe(self):
#         a = []
#         for i in self.tomatoes:
#             if i.index == 4:
#                 a.append(True)
#             else:
#                 a.append(False)
#             return a
        
#     def give_away_all(self):
#         self.tomatoes.clear


# class Gardener:
#     def __init__(self, name: str, plant = Tomatobush()) -> None:
#         self.name = name 
        
#     def work(self):
#         for i in self.plant:
#             i.self.grow_all()
#             print(f'Помидоры стали более зрелыми')


#     def harvest(self):
#         for i in self.tomatoes:
#             if i.index == 4:
#                 print('Все плоды созрели,можно собирать')
#             else:
#                 print('Они еще не созрели')
    
# tomat = Tomato('tomat')
# name = Gardener('Jon',[2])
# t = Tomatobush([1])

# print()



class Product:
    def __init__(self, name = str, category = str, price = int) -> None:
        self.name = name 
        self.category = category
        self.price = price 
        
class Shelf:
    def __init__(self,number = int, capacity = str, product1 = Product()) -> None:
        self.number = number 
        self.capacity = capacity
        self.product1 = product1 
        
    def _check_polk(self):
        for pro in self.product1:
            if pro <= 4:
                return f'У вас все вместилось'
            else:
                return f'НЕ ВМЕСТИТЬСЯ!'
            
    def _get_products(self):
        return self.product1
    

class Magazin:
    def __init__(self, name = str, shelf = Shelf()) -> None:
        self.name = name 
        self.shelf = shelf 
        
    def _get_products_all(self):
        return self.shelf 
        
    def _get_product_price(self):
        dict1 = {
            'Куртка': 1200,
            'Рубашка': 890,
            'Платье': 1000,
            'Кофта': 2000
        }
        return f'{self._get_product_price}'
    
    
    def _get_all_price(self):
        sum = 0 
        for value in dict1:
            sum += dict1 
        return sum
    
    def _get_categories(self):
        return self.name


s = Shelf(123,'Одежды',['платье','Одежды',1000])
d = Magazin('qwerty')
w = Magazin()

# print(s._get_products())
# print(d._get_all_price())
# print(s._check_polk())
# print(dict1)
# print(d._get_categories())

