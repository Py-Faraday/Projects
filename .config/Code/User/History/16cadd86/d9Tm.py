
from urllib import request
from config import API

sity = "Bishkek"

url = f"http://api.openweathermap.org/data/2.5/weather?q={sity}&appid={API}&units=metric"

r=request.get(url)
print(r)
