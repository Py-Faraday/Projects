import requests


def get_epizody()->list:
    url='https://rickandmortyapi.com/api/location'
    r =requests.get(url)