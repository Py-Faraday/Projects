import requests
def get_list_location()->list:
    url='https://rickandmortyapi.com/api/location'
    r =requests.get(url)
    

    data=r.json()['results']
    return data
def get_location_names()->list:
    return[i['name']for i in get_list_location()]
print(get_location_names())
