import requests

# url="https://rickandmortyapi.com/api"
url='https://rickandmortyapi.com/api/character'

r=requests.get(url)

print(r.text)

# with open ('url.txt','w') as file:
#     file.write(r.text)