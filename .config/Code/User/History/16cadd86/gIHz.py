
import requests
from config import API

sity = "Bishkek"

url = f"http://api.openweathermap.org/data/2.5/weather?q={sity}&appid={API}&units=metric"

r=requests.get(url)
s=r.json()
pprint(s)


sity=s['name']
cur_weather=data['main']['temp']
