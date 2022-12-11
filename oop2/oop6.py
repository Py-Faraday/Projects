# class Home:
#     def __init__(self,nm: name = 'Shoto', age = 19, surname = 'Todoroki') -> None:
#         self.name = name
#         self.age = age 
#         self.surname = surname
        
#     def information(self):
#         return f'{self.age}'
    
# home = Home('Sho', 67, 'Todor')
# print(home.information())



# class Math:
#     def __init__(self,a , b) -> None:
#         self.a = a 
#         self.b = b 
        
#     def umno(self):
#         return self.a * self.b 
    
# math = Math(23, 89)
# print(math.umno())


# class Students:
#     def __init__(self, name = 'Ria', last_name = 'Sadakova', department = 'Программирования', year = 2022) -> None:
#         self.name = name 
#         self.last_name = last_name
#         self.department = department
#         self.year = year 
        
#     def informa(self):
#         return f'{self.name} {self.last_name} поступил на факультет {self.department} в {self.year}'
    
# s = Students()
# a = Students("arkadii","merisov","java",2000)
# print(s.informa())
# print(a.informa())

class Soda:
    def __init__(self,type_limonads = list()) -> None:
        self.type_limonads = type_limonads
        
    def show_my_drink(self):
        for i in self.type_limonads:
            if i == "малина":
                print("есть")
            else:
                print('netu')

soda = Soda(["кофе","малина"]) 
print(soda.show_my_drink())    
