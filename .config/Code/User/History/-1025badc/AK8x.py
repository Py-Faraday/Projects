





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
    # print(f'{di=},{name=}, {status=}, {origin}')
with open ('write.txt','a') as file:
    file.write(f'№{str(di)} Name: {name}, Status:{status}, Origin:{origin}\n')