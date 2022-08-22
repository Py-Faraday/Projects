from unicodedata import name
import requests
import json
from pprint import pprint


# url="https://rickandmortyapi.com/api"
url='https://rickandmortyapi.com/api/character/2'

r=requests.get(url)

data=r.json
print(data['name'])



# with open ('url.txt','w') as file:
#     file.write(r.text)