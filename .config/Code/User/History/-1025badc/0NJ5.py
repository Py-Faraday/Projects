from pprint import pprint

import requests
from config import API
from datetime import datetime


 


city = "Bishkek"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"

r = requests.get(url)
data = r.json()

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

# city = data['name']
# cur_weather = data['main']['temp']
# humidity = data['main']['humidity']
# pressure = data['main']['pressure']
# wind = data['wind']['speed']
# sunrise_timepesmp = \
#     datetime.fromtimestamp(data['sys']['sunrise'])
# sunset_timepesmp = \
#     datetime.fromtimestamp(data['sys']['sunset'])
# length_of_the_day = sunrise_timepesmp - sunset_timepesmp
# weather_description = data['weather'][0]['main']


def pop(sity):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={sity}&appid={API}&units=metric"
        r=requests.get(url)
        data=r.json()
        text=f'''
        Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Погода в городе: {data['name']}
        Температура: {data['main']['temp']}
        Влажность: {data['main']['humidity']}
        Давление: {data['main']['pressure']} мм.рт.ст
        Скорость ветра: {data['wind']['speed']}
        Восход: {datetime.fromtimestamp(data['sys']['sunrise'])}
        Закат: {datetime.fromtimestamp(data['sys']['sunset'])}
        '''
        return text
    except Exception:
        return 'wrong'






