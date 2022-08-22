import requests


def get_epizody()->list:
    url='https://rickandmortyapi.com/api/location'
    r =requests.get(url)

    data=r.json()['results']
    return data
def get_epizody()->list:
    return[i['name']for i in get_epizody()]

def get_epizody(name:str)->dict:
    epizods={i['name']:i['id']for i in get_epizody()}
    epiz_id=epizods[name]
    url =f'https://rickandmortyapi.com/api/location/{loc_id}'
    data=requests.get(url).json()
    return data