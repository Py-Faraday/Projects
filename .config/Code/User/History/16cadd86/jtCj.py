import requests
from config import API

city='Bishkek'
url='https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}'

r=requests.