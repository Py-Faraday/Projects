
class Mebel:
    def __init__(self, name:str, area: int, price: int) -> None:
        self.name = name
        self.area = area
        self.price = price

    def __str__(self) -> str:
        return self.name


class Home:
    def __init__(self, name: str, area: int, price: int, list_mebel: Mebel = []) -> None:
        self.name = name
        self.area = area
        self.list_mebel = list_mebel
        self.price = price

    def get_area(self):
        summ = 0
        for mebel in self.list_mebel:
            summ += mebel.area
        return self.area - summ

    def get_mebels_name(self):
        names = []
        for mebel in self.list_mebel:
            names.append(mebel.name)
        return names

    def get_mebels_price(self):
        summa = 0
        for mebel in self.list_mebel:
            summa += mebel.price
        return summa

    def get_full_price(self):
        full = self.get_mebels_price() + self.price
        return full

    def __str__(self) -> str:
        return self.name



class Humanoid:
    def __init__(self,name: str, balance: int, list_home: Home = []) -> None:
        self.name = name
        self.balance = balance
        self.list_home = list_home

    def __str__(self) -> str:
        return self.name

    def get_home_names(self):
        home = []
        for my_home in self.list_home:
            home.append(my_home.name)
        return home

    def buy_home(self, home):
        if self.balance >= home.get_full_price():
            self.balance -= home.get_full_price()
            self.list_home.append(home)
            print(f'{self.name}, купил дом "{home.name}" за {home.get_full_price()} $')
        else:
            print(f'чтобы купить дом "{home.name}" вам не хватает денег')



