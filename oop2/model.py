from oop5 import Mebel,Home,Person

# wardrode = Mebel('Home2', 3,1234)
# table = Mebel('Home3', 90,567)
# sofa = Mebel('Home4', 6,234)
# home89 = Home('home34', 43, 12000,[table,sofa,wardrode])


home78 = Person('home90', 79000)
home12 = Person('home456', 234567)
home99 = Person('name', 23000, [home12, home78])
home99.balance += 100000
print(home99.buy_home())