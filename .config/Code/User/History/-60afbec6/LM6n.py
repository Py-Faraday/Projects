
from random import choice
students = ['Каныкей','Бексултан' ,'Айбарчын' ,'Тилек' ,'Арген' ,'Байзак' ,'Актан' ,'Эгида ','Байель' ,'Нурдик ','Искен']
team1=[]
team2=[]
for i in students:
    while len(team1)!=6:
        name = choice(students)
        if name not in team1:
            team1.append(name)
    print(name)