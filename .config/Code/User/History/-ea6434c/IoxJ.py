import requests

url = 'https://back.detox.today/api/v1/products/'
r=requests.get(url).json()
# print(r[0]['title'])
def func():
    a=[]
    for i in r:
        a.append(i['title'])
    return a
print(func())