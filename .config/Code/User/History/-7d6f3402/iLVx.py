import requests


def get_epizody()->list:
    url='https://rickandmortyapi.com/api/location'
    r =requests.get(url)

    data=r.json()['results']
    return data
def get_epizody()->list:
    return[i['name']for i in get_epizody()]