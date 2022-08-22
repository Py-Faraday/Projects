import requests
url='https://rickandmortyapi.com/api/location'
r =requests.get(url)

print(r.json())
