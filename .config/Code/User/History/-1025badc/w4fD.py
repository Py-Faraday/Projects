





import requests

url = "https://rickandmortyapi.com/api/character/"

r = requests.get(url)

data = r.json()
data = data['results']

for i in data:
    di=i['id']
    name = i['name']
    status = i['status']
    origin = i['location']['name']
    print(f'id={di=},{name=}, {status=}, {origin}')
with open ('write.txt','w')as url:
    url.write(di)
    url.write(name)
    url.write(status)
    url.write(origin)