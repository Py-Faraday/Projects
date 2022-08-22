# tasks1 = {
#     'Задание №1': """
#             Создать Дебильный Калькулятор
#         Который будет запрашивать у пользователя один из выражений (+,-,/,*,**, //,%)
#         После он должен спросить первую цифры за тем вторую .
#         В зависимости от того что выбрал пользователь Необходимо совершить выражение и показать ответ

#         Пример
#         Пользователь выбирает : *
#         Первую цифру: 6
#         Вторую цифру: 5
#         Ответ: 30
#         Примечание:
#         Задания может быть выполнена без использования цикла
#         Можно использовать  условные операторы, input()
#         Типы данных: int, str, float
#     """,
#     'Задание №2': """
#             Есть список 
#         a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
#         1.Добавьте в список ещё одну цифру 13
#         2.Узнайте сколько раз встречается цифра 13
#         3.узнайте длину списка а
#         4.узнайте сколько процентов списка занимает цифра 13 формула (количество цифры 13 * 100 / длина списка)
#                 Если процент будет меньше 70% вывести: НЕУЖЕЛИ
#                 Если будет больше 70% вывести: Я ТАК И ЗНАЛ
#                 Если равен 70% вывести : СОВПАДЕНИЕ ? НЕ ДУМАЮ

#         Примечание:
#         Задания может быть выполнена без использования цикла
#         Можно использовать методы листа и условные операторы
    
#     """,
#     'Задание №3': """
#         1. Зарегистрируйте пользователя запросив логин и пароль
#         2. Добавьте полученные данные в список users = [ ]
#         3. Попросите Пользователя Войти запросив пороль и логин 
#         4. если данные есть в списке users выведите ДОБРО ПОЖАЛОВАТЬ 
#         5. Если данные не окажутся или были введены неправильные данные выведите НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ
#     """,
# }

# tasks2 = {
#     'Задание №1': """
#             1 Практика методов ключ значение
#             Написать скрипт который проходится по ключам и проверяет значения
#             a) Если значение делиться на 3, то записываем строку “Hi”
#             b) Если значение делиться на 5, то записываем строку “Bye”
#             ПРИМЕР:
#             Дано -> dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
#             Результат -> a = Bye
#             b = Hi""",
#     'Задание №2': """
#         4. Напишите код, который выведет на экран список языков с нумерацией.
#          languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#             Вывод:
#             0 go
#             1 java
#             2 php
#             3 python
#             4 javascript
#             5 ruby

#         """,
#     'Задание №3': """
#             Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, 
#             то получим 3, 5, 6 и 9. 
#             Сумма этих чисел равна 23 (3+5+6+9) = 23.
#             Найдите сумму всех чисел меньше 1000, кратных 3 или 5.""",
#     'Задание №4': """
#             Если взять строку - "237" и сложить все её числа то получится 2+3+7 = 12.
#             Возьмите строку "4729461084" и сложите все её числа.
#             Результат выведите на экран.""",
#     'Задание №5': """
#             Создайте input() который принимает от пользователя 
#             дату в формате: "2020-10-24 18:30" и возвращает dictionary 
#             разделённую по значениям даты:

#             date = {
#             "year": "2020",
#             "month": "10",
#             .....
#             }""",
#     'Задание №6': """
#             Напишите проверку на то, является ли строка палиндромом.
#             Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
            
#             # Пример:
#                     # тот -> тот
#                     # потоп -> потоп
#                     # көк -> көк
            
            
#             # СЛОВА ДЛЯ ПРОВЕРКИ:
#             words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопк    у',]
#             """
# }

# final = {
#     'task': """Списки. Города

#             Выберите действие:
#             1. Добавить новый город
#             2. Отобразить список городов
#             3. Заменить город
#             4. Удалить город
#             5. Выход

#             Ваше действие: 1

#             Введите название города: Нью Йорк
#             а .Город добавлен!
#             б. Такой город уже есть! Нью Йорк - 3
#             в. Некорректное название!

#             Выберите действие:
#             1. Добавить новый город
#             2. Отобразить список городов
#             3. Заменить город
#             4. Удалить город
#             5. Посетить следующий город
#             6. Выход

#             Ваше действие: 2

#             Список городов:
#             1. Нью Йорк

#             Выберите действие:
#             1. Добавить новый город
#             2. Отобразить список городов
#             3. Заменить город
#             4. Удалить город
#             5. Посетить следующий город
#             6. Выход

#             Ваше действие: 3

#             Текущий город: Нью Йорк
#             Новый город: Нарын
#             а. Текущий город отсутствует.
#             б. Город заменен.
#             в. Такой город уже есть! Нью Йорк - 3
#             г. Некорректное название!

#             Выберите действие:
#             1. Добавить новый город
#             2. Отобразить список городов
#             3. Заменить город
#             4. Удалить город
#             5. Посетить следующий город
#             6. Выход

#             Ваше действие: 4

#             Введите название города: Нарын
#             а. Текущий город отсутствует.
#             б. Некорректное название!
#             в. Город удален!



#             Выберите действие:
#             1. Добавить новый город
#             2. Отобразить список городов
#             3. Заменить город
#             4. Удалить город
#             5. Посетить следующий город
#             6. Выход 
 

# Ваше действие: 5
# Программа завершает работу."""
# }

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in enumerate(languages):
#         print (i)






import subprocess
import os
import re
from collections import namedtuple
import configparser


def get_windows_saved_ssids():
    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = []
    profiles = re.findall(r"Весь профиль пользователя\s(.*)", output)
    for profile in profiles:
        ssid = profile.strip().strip(":").strip()
        ssids.append(ssid)
    return ssids


def get_windows_saved_wifi_passwords(verbose=1):
    ssids = get_windows_saved_ssids()
    Profile = namedtuple("Profile", ["ssid", "ciphers", "key"])
    profiles = []
    for ssid in ssids:
        ssid_details = subprocess.check_output(f"""netsh wlan show profile "{ssid}" key=clear""").decode()
        ciphers = re.findall(r"Cipher\s(.*)", ssid_details)
        ciphers = "/".join([c.strip().strip(":").strip() for c in ciphers])
        key = re.findall(r"Key Content\s(.*)", ssid_details)
        try:
            key = key[0].strip().strip(":").strip()
        except IndexError:
            key = "None"
        profile = Profile(ssid=ssid, ciphers=ciphers, key=key)
        if verbose >= 1:
            print_windows_profile(profile)
        profiles.append(profile)
    return profiles


def print_windows_profile(profile):
    print(f"{profile.ssid:25}{profile.ciphers:15}{profile.key:50}")


def print_windows_profiles(verbose):
    print("SSID                     CIPHER(S)      KEY")
    get_windows_saved_wifi_passwords(verbose)


def get_linux_saved_wifi_passwords(verbose=1):
    network_connections_path = "/etc/NetworkManager/system-connections/"
    fields = ["ssid", "auth-alg", "key-mgmt", "psk"]
    Profile = namedtuple("Profile", [f.replace("-", "_") for f in fields])
    profiles = []
    for file in os.listdir(network_connections_path):
        data = { k.replace("-", "_"): None for k in fields }
        config = configparser.ConfigParser()
        config.read(os.path.join(network_connections_path, file))
        for _, section in config.items():
            for k, v in section.items():
                if k in fields:
                    data[k.replace("-", "_")] = v
        profile = Profile(**data)
        if verbose >= 1:
            print_linux_profile(profile)
        profiles.append(profile)
    return profiles


def print_linux_profile(profile):
    print(f"{str(profile.ssid):25}{str(profile.auth_alg):5}{str(profile.key_mgmt):10}{str(profile.psk):50}") 


def print_linux_profiles(verbose):
    print("SSID                     AUTH KEY-MGMT  PSK")
    get_linux_saved_wifi_passwords(verbose)
    
    
def print_profiles(verbose=1):
    if os.name == "nt":
        print_windows_profiles(verbose)
    elif os.name == "posix":
        print_linux_profiles(verbose)
    else:
        raise NotImplemented("Код работает только для ОС Linux or Windows")
    
    
if __name__ == "__main__":
    print_profiles()