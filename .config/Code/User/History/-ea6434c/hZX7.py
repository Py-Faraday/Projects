import requests

url = 'https://back.detox.today/api/v1/image/'
r=requests.get(url).json()
print(r[0]['title'])