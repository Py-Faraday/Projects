





import requests

url = "https://rickandmortyapi.com/api/character/"

r = requests.get(url)

data = r.json()
data = data['results']

for i in data:
    name = i['name']
    status = i['status']
    origin = i['location']['name']
    print(name, status, origin)