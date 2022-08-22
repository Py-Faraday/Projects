import requests

url = 'https://back.detox.today/api/v1/image/'
r=requests.get(url).json()
# print(r[0]['title'])
def func():
    for i in url:
        if i=="title":
            return i
print(func())