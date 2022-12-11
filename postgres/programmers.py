import psycopg2
import random as rd
from data import logins, professions, countries, pswd_symbols, streets


def connect(db_name: str, user: str, password: str, host: str = 'localhost'):
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host
    )
    return conn



def generate_password():
    password_list = []
    
    for _ in range(5000):
        password = ''
        for _ in range(rd.randint(8, 16)):
            password += rd.choice(pswd_symbols)
        password_list.append(password)

    return password_list

def generate_email(logins: list) -> list:
    domen = ("@gmail.com", "@mail.ru", "@yandex.kz", "@yandex.kg", "@bk.ru")
    email_list = []

    for name in logins:
        email_list.append(name+rd.choice(domen))
    
    return email_list


def generate_phone() -> list:
    codes = ("50", "77", "55", "99", "70", "22", "20")
    phone_list = []
    
    for _ in range(5000):
        number = '+996'+ rd.choice(codes) + str(rd.randint(1000000, 9999999))
        phone_list.append(number)

    return phone_list


def generate_streets(sreetes: list) -> list:
    street_list = []
    for _ in range(5000):
        address = rd.choice(streets)+ ' ' + str(rd.randint(1, 150))
        street_list.append(address)
    return street_list


def create_table(conn: object) -> None:
    query = """
    CREATE TABLE users(
        id SERIAL PRIMARY KEY,
        login VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        phone VARCHAR(50) NOT NULL,
        country VARCHAR(50) NOT NULL,
        address VARCHAR(50) NOT NULL,
        profession VARCHAR(50) NOT NULL,
        followers INT NOT NULL
    );
    """
    cursor = conn.cursor()
    cursor.execute(query)
    print("Table created success")
    conn.commit()
    
    
def inser(conn: object, logins: list , passwords: list, emails: list, 
            phones: list, countries: list, addresses: list, professions: list):

    query = """INSERT INTO users(
        login, password, email, phone, country, address, profession, followers
    )
    VALUES """

    for _ in range(10000):
        query += f"""(
        '{rd.choice(logins)}',
        '{rd.choice(passwords)}',
        '{rd.choice(emails)}',
        '{rd.choice(phones)}',
        '{rd.choice(countries)}',
        '{rd.choice(addresses)}',
        '{rd.choice(professions)}',
        {rd.randint(1, 10000000)}
        ),"""
    
    query = query[:-1] + ';'
    print(query)
    cursor = conn.cursor()
    cursor.execute(query)
    print("ISERT success")
    conn.commit()
    cursor.close()
    conn.close()


logins = logins
passwords = generate_password()
emails = generate_email(logins)
phones = generate_phone()
countries = countries
addresses = generate_streets(streets)
professions = professions