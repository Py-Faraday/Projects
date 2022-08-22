from unicodedata import name
import requests
import json
from pprint import pprint


# url="https://rickandmortyapi.com/api"
url='https://rickandmortyapi.com/api/character/2'

r=requests.get(url)

data=r.json()
data =data['result']
for i in data:
    name=i['name']
    status=i['status']
    origin=i['location']['name']
    print(name,status,origin)

# name=data['name']
# status=data['status']

# print(name)

# print(status)



# # with open ('url.txt','w') as file:
# #     file.write(r.text)