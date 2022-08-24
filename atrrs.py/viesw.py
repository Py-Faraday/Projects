# from database import home1, home2, person1, shkaf, stol, divan
# print(home1.full_price())
# print(person1.balance)
# person1.balance += 10000

# print(person1.balance)
# person1.buy_home(home1)

# print(person1.balance)
# person1.balance +=10000
# print(person1.get_home_names())
# print(person1.get_home_names())


from database import home1, home2, person1, shkaf, stol, divan


print(home1.full_price())
print(person1.balance)
person1.balance += 10000

print(person1.balance)
person1.buy_home(home1)

print(person1.balance)
person1.balance += 100000 
print(person1.get_home_names())


person1.buy_home(home2)
print(person1.get_home_names())
