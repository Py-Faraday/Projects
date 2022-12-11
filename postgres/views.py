from programmers import (
    connect, 
    create_table, 
    inser,
    logins,
    passwords,
    emails,
    phones,
    countries,
    addresses,
    professions
)

# password = input("Введите пароль от Базы Данных: \n >>> ")

conn = connect(
    db_name='sukuna',
    user='itadori',
    password='1234'
)

create_table(conn=conn)
inser(
    conn=conn,
    logins=logins,
    passwords=passwords,
    emails=emails,
    phones=phones,
    countries=countries,
    addresses=addresses,
    professions=professions
) 
