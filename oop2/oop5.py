class Mebel:
    def __init__(self,name: str,area: int, price:int ) -> None:
        self.name = name 
        self.area = area 
        self.price = price 
    
    def __str__(self) -> str:
        return self.name


class Home:
    def __init__(self,name: str,area: int,price: int, list_mebel: Mebel = []) -> None:
        self.name = name 
        self.area = area 
        self.price = price
        self.list_mebel = list_mebel

    def get_area(self):
        summ = 0
        for mebel in self.list_mebel:
            summ += mebel.area
        return self.area - summ
    
    def get_names(self):
        nm = []
        for home in self.list_mebel:
            nm.append(home.name)
        return nm
    
    def get_mebel_price(self):
        sum = 0 
        for mebel in self.list_mebel:
            sum += mebel.price
        return sum

    def full_price(self):
        return self.price + self.get_mebel_price()

    def __str__(self) -> str:
        return self.name

class Person:
    def __init__(self,name:str, balance: int, home_list: Home = [] ) -> None:
        self.name = name 
        self.balance = balance
        self.home_list = home_list 
    
    def __str__(self) -> str:
        return self.name
      
    def get_names_home(self):
        ns = []
        for person in self.home_list:
            ns.append(person.name)
        return ns 
    
    def buy_home(self,home):
        if self.balance >= home.full_price():
            self.balance - home.full_price()
            self.home_list.append(home)
            return f'{self.name} купили {home.name}этот дом за столько {home.full_price()}'
        else:
            return f'Вы не можете купить этот дом'          

