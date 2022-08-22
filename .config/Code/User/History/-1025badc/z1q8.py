import requests

url="https://rickandmortyapi.com/api"

r=requests.get(url)

print(r)