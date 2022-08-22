# # import requests
# # import json
# # from pprint import pprint

# # # url = "https://rickandmortyapi.com/api"
# # url = "https://rickandmortyapi.com/api/character/"
# # # url = 'https://developer.mozilla.org/ru/docs/Web/HTTP/Status'

# # r = requests.get(url)
# # data = r.json()
# # data = data['results']


# # for i in data:
# #     idd = i['id']
# #     name = i['name']
# #     status = i['status']
# #     origin = i['location']['name']
# #     print(name,status,origin)
    
# #     with open('url.txt','a+') as file:
# #         file.write(f'{idd} - {name} Satus: {status} Origin: {origin} \n')
        
        
# # # print(origin)


# # import requests
# # import json
# # from pprint import pprint

# # # url = "https://rickandmortyapi.com/api"
# # url = "https://rickandmortyapi.com/api/character/"
# # # url = 'https://developer.mozilla.org/ru/docs/Web/HTTP/Status'

# # r = requests.get(url)
# # data = r.json()
# # data = data['results']


# # for i in data:
# #     idd = i['id']
# #     name = i['name']
# #     status = i['status']
# #     origin = i['location']['name']
# #     print(name,status,origin)
    
# #     with open('url.txt','a+') as file:
# #         file.write(f'{idd} - {name} Satus: {status} Origin: {origin} \n')
        
        
# # # print(origin)

# from pprint import pprint
# from config import API
# import requests
# from datetime import datetime

# city = "Bishkek"

# url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
# r = requests.get(url)
# data = r.json()
# pprint(data)

# city = data['name']
# c_weather = data['main']['temp']
# humidity = data['main']['humidity']
# pressure = data['main']['pressure']
# wind = data['wind']['speed']
# sunrise_time = \
#     datetime.fromtimestamp(data['sys']['sunrise'])
# sunset_time = \
#     datetime.fromtimestamp(data['sys']['sunset'])
# lenght_of_the = sunrise_time - sunset_time 
# weather_description = data['weather'][0]['main']


# text = f'''
# Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Погода в городе:{city}
# Температура:{c_weather}
# Влажность:{humidity}
# Давление:{pressure}мм.рт.ст
# Скорость ветра:{wind}
# Продолжительность дня:{lenght_of_the}
# Закат:{sunset_time}

# '''
# pprint(data)




# import requests
# from config import API
# from datetime import datetime


# def pop(city):
#     try:
#         url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
#         r = requests.get(url)
#         data = r.json()
#         text = f'''
#         Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
#         Погода в городе: {data['name']}
#         Температура: {data['main']['temp']}
#         Влажность: {data['main']['humidity']}
#         Давление: {data['main']['pressure']} мм.рт.ст
#         Скорость ветра: {data['wind']['speed']}
#         Восход: {datetime.fromtimestamp(data['sys']['sunrise'])}
#         Закат: {datetime.fromtimestamp(data['sys']['sunset'])}
#         '''
#         return text
#     except Exception:
#         return 'Такого города нет'
    
    