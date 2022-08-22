import requests



url = 'https://back.detox.today/api/v1/image/'
r = requests.get(url).json()

def my_title():
    a = []
    for i in r:
        a.append(i['title'])
    return a
        
print(my_title())

