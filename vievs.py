from datebase import home1,home2,human,earth,marsianin,shkaf,stol,divan

print(home1.get_full_price())
print(earth.get_full_price())

print(f'у персонажа {human} есть {human.balance} $ ')
print(f'у персонажа {marsianin} есть {marsianin.balance} $ ')
# human.balance += 10

human.buy_home(home1)
marsianin.buy_home(earth)

print(human.balance)
print(marsianin.balance)

print(human.get_home_names())
print(marsianin.get_home_names())
