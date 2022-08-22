import requests

url = 'https://back.detox.today/api/v1/image/'
r=requests.get(url).json()
# print(r[0]['title'])
def func():
    a=[]
    for i in r:
        a.append(i['id'])
    return a
print(func())