# from mebel import Home, Mebel, Person
# shkaf = Mebel('shkaf',2,12000)
# stol = Mebel('stol',4,8999)
# divan = Mebel('divan',3,22000)
# home1 = Home('Odin doma', 35, 500000,[stol, shkaf])
# home2 = Home('Dom 2', 54, 600000)
# home1.list_mebel.append(stol)
# home2.list_mebel = [divan,shkaf]
# person = Person('asan',600000)
# # marsianin = Humanoid('marsianin',100000000000000)
# #earth = Home('earth',510100000,1000000000000)

# # home2.list_mebel = [divan, divan, shkaf, divan]



from models import Home, Mebel, Person


shkaf = Mebel('Shkaf', 2, 1200)
stol = Mebel('Stol', 3, 2000)
divan = Mebel('Divan', 5, 5000) 
    
home1 = Home('Home_12', 18,10000, [stol,shkaf,divan])
home2 = Home('Dom', 23, 12000)

home2.list_mebel.append(stol)
home2.list_mebel = [divan,shkaf]

person1 = Person('Den', 12000)