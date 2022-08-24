# class Mebel:
#     def __init__(self, name: str, area: int, price: int) -> None:
#         self.name=name
#         self.area=area
#         self.price=price
#     def __str__(self) -> str:
#         return self.name
# class Home:
#     def __init__(self, name: str, area: int, list_mebel: Mebel=[]) -> None:
#         self.name=name
#         self.area=area
#         self.list_mebel=list_mebel
#     def get_area(self):
#         summ=0
#         for mebel in self.list_mebel:
#             summ += mebel.area
#         return self.area - summ

#     def get_mebel_name(self):
#         names=[]
#         for mebel in self.list_mebel:
#             names.append(mebel.name)
#         return names

#     def get_mebel_price(self):
#         summ=0
#         for mebel in self.list_mebel:
#             summ+=mebel.price
#         return summ 
#     def __str__(self)-> str:
#         return self.name
# class Beka:
#     def __init__(self, name: str, home: Home, balance: int ) ->None:
#         self.name=name
#         self.home=home
#         self.balance=balance
#     def get_home_names(self):
        



# # shkaf=Mebel('SHkaf', 2, 4700)
# # stol=Mebel('Stol', 4 ,7402)
# # divan=Mebel('Divan', 3, 7900)
# # print(shkaf.area)
# home1=Home('Dom 312', 35, [stol,shkaf])
# home2=Home('Dom 313', 54)
# home2.list_mebel.append(stol)
# home2.list_mebel=[divan, divan, shkaf]
# # # print(home1.get_area())
# # print(home1.get_mebel_name())
# # print(home2.get_mebel_name())
# home2=Home('Dom 313', 54)
# # print(dir(home2))
# print(home1.get_mebel_price())


# class Mebel: 
#     def init(self,name3: str, area: int, price: int) -> None:
#         self.name = name 
#         self.area = area
#         # print(self)
#         self.price = price
        
#     def str(self) -> str:
#         return self.name


# class Home:
#     def  init(self,name2: str, area:int, price: int,list_mebel:Mebel = []) -> None:
#         self.name = name 
#         self.area = area 
#         self.price = price
#         self.list_mebel = list_mebel 
        
        
#     def get_area(self):
#         summ = 0
#         for mebel in self.list_mebel:
#             summ += mebel.area
#         return self.area - summ
    
#     def get_name(self):
#         names = []
#         for mebel in self.list_mebel:
#             names.append(mebel.name)
#         return names
        
    
#     def get_price(self):
#         sum = 0 
#         for mebel in self.list_mebel:
#             sum += mebel.price
#         return sum
    
#     def full_price(self):
#         return self.price + self.get_price()
    

        
#     def __str__ (self) -> str:
#         return self.name
    
# shkaf = Mebel('Shkaf',2,1200)
# stol = Mebel('Stol', 3,2000)
# divan = Mebel('Divan', 5,5000) 
    
# home1 = Home('Home_12', 18,10000,[stol,shkaf,divan])
# home2 = Home('Dom', 23,12000) 
# home2.list_mebel.append(stol)
# home2.list_mebel = [divan,shkaf]

         
    
# class Person:
#     def __init__(self,name1: str, balance: int, home_list: Home = []) -> None:
#          self.name = name
#          self.balance = balance
#          self.home_list = home_list
         
#     def __str__(self) -> str:
#         return self.name
    
#     def get_home_names(self):
#         nm = []
#         for home in self.home_list:
#             nm.append(home.name)
#         return 
    
#     def buy_home(self, home):
#         if self.balance>= home.full_price():
#             self.balance-=home.full_price()
#             self.home_list.append(home)
#             print(f"{self.name} buy home {home.name} at price {home.full_price()}")
#         else:
#             print("You cannot buy this home !!!")



#         return f'{self_name1} купил {self_nzme2} за '
    
# person1 = Person('Den',12000,[home1,home2])
# print(person1.get_home_names())


class Mebel: 
    def __init__(self, name: str, area: int, price: int) -> None:
        self.name = name 
        self.area = area
        self.price = price
        
    def __str__(self) -> str:
        return self.name


class Home:
    def  __init__(self, name: str, area:int, price: int,list_mebel:Mebel = []) -> None:
        self.name = name 
        self.area = area 
        self.price = price
        self.list_mebel = list_mebel 
        
        
    def get_area(self):
        summ = 0
        for mebel in self.list_mebel:
            summ += mebel.area
        return self.area - summ
    
    def get_name(self):
        names = []
        for mebel in self.list_mebel:
            names.append(mebel.name)
        return names
        
    
    def get_price(self):
        sum = 0 
        for mebel in self.list_mebel:
            sum += mebel.price
        return sum
    
    def full_price(self):
        return self.price + self.get_price()
    

        
    def __str__(self) -> str:
        return self.name
    


         
    
class Person:
    def __init__(self, name: str, balance: int, home_list: Home = []) -> None:
         self.name = name
         self.balance = balance
         self.home_list = home_list
         
    def __str__(self) -> str:
        return self.name
    
    def get_home_names(self):
        nm = []
        for home in self.home_list:
            nm.append(home.name)
        return nm 
    
    def buy_home(self, home):
        if self.balance >= home.full_price():
            self.balance -= home.full_price()
            self.home_list.append(home)
            print(f"{self.name} buy home {home.name} at price {home.full_price()}")
        else:
            print("You cannot buy this home !!!")