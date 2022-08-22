import requests
from pprint import pprint

# url="https://rickandmortyapi.com/api"
url='https://rickandmortyapi.com/api/character'

r=requests.get(url)

data=r.text
pprint(data)


# with open ('url.txt','w') as file:
#     file.write(r.text)