
from pprint import pprint

import requests
from config import API
from datetime import datetime


# city = "Bishkek"

# url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"

# r = requests.get(url)
# data = r.json()
# pprint(data)
# # {'base': 'stations',
# # 'clouds': {'all': 4},
# # 'cod': 200,
# # 'coord': {'lat': 42.87, 'lon': 74.59},
# # 'dt': 1660717137,
# # 'id': 1528675,
# # 'main': {'feels_like': 26.11,
# #          'grnd_level': 927,
# #          'humidity': 17,
# #          'pressure': 1010,
# #          'sea_level': 1010,
# #          'temp': 26.11,
# #          'temp_max': 26.11,
# #          'temp_min': 26.11},
# # 'name': 'Bishkek',
# # 'sys': {'country': 'KG',
# #         'id': 8871,
# #         'sunrise': 1660694978,
# #         'sunset': 1660744935,
# #         'type': 1},
# # 'timezone': 21600,
# # 'visibility': 10000,
# # 'weather': [{'description': 'clear sky',
# #              'icon': '01d',
# #              'id': 800,
# #              'main': 'Clear'}],
# # 'wind': {'deg': 340, 'gust': 2.96, 'speed': 3.57}}

# city = data['name']
# cur_weather = data['main']['temp']
# humidity = data['main']['humidity']
# pressure = data['main']['pressure']
# wind = data['wind']['speed']
# sunrise_timepesmp = \
#     datetime.fromtimestamp(data['sys']['sunrise'])
# sunset_timepesmp = \
#     datetime.fromtimestamp(data['sys']['sunset'])
# length_of_the_day = sunset_timepesmp - sunrise_timepesmp
# weather_description = data['weather'][0]['main']

# text=f'''
# date:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# pogoda v gorode:{city}
# temp:{cur_weather}
# vlajnost:{humidity}
# davlen:{pressure}мм.рт.ст 
# skorost vetra:{wind}
# vosxod:{sunrise_timepesmp}
# prodolj dnia:{length_of_the_day}
# zakat:{sunset_timepesmp}
# '''
# print(text)







def pogoda(url):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"

    r = requests.get(url)
    data = r.json()
    pprint(data)
# {'base': 'stations',
# 'clouds': {'all': 4},
# 'cod': 200,
# 'coord': {'lat': 42.87, 'lon': 74.59},
# 'dt': 1660717137,
# 'id': 1528675,
# 'main': {'feels_like': 26.11,
#          'grnd_level': 927,
#          'humidity': 17,
#          'pressure': 1010,
#          'sea_level': 1010,
#          'temp': 26.11,
#          'temp_max': 26.11,
#          'temp_min': 26.11},
# 'name': 'Bishkek',
# 'sys': {'country': 'KG',
#         'id': 8871,
#         'sunrise': 1660694978,
#         'sunset': 1660744935,
#         'type': 1},
# 'timezone': 21600,
# 'visibility': 10000,
# 'weather': [{'description': 'clear sky',
#              'icon': '01d',
#              'id': 800,
#              'main': 'Clear'}],
# 'wind': {'deg': 340, 'gust': 2.96, 'speed': 3.57}}

    city = data['name']
    cur_weather = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    sunrise_timepesmp = \
        datetime.fromtimestamp(data['sys']['sunrise'])
    sunset_timepesmp = \
        datetime.fromtimestamp(data['sys']['sunset'])
    length_of_the_day = sunset_timepesmp - sunrise_timepesmp
    weather_description = data['weather'][0]['main']

    text=f'''
    date:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    pogoda v gorode:{city}
    temp:{cur_weather}
    vlajnost:{humidity}
    davlen:{pressure}мм.рт.ст 
    skorost vetra:{wind}
    vosxod:{sunrise_timepesmp}
    prodolj dnia:{length_of_the_day}
    zakat:{sunset_timepesmp}
    '''
    return pogoda("Osh")
