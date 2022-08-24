from mebel import Home, Mebel, Humanoid


shkaf = Mebel('shkaf', 2 , 12000)
stol = Mebel('stol' , 4 , 8999)
divan = Mebel('divan' , 3 , 22000)

home1 = Home('Odin doma', 35 , 500000 ,[stol, shkaf])
home2 = Home('Dom 2', 54 , 600000)
earth = Home('earth', 510100000, 1000000000000)

home2.list_mebel = [divan, divan, shkaf, divan]

human = Humanoid('bob', 600000)
marsianin = Humanoid('marsianin', 100000000000000)


home2.list_mebel = [divan, divan, shkaf, divan]


