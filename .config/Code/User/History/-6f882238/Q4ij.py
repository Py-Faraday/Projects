import requests
def get_list_location()->list:
    url='https://rickandmortyapi.com/api/location'
    r =requests.get(url)
    

    data=r.json()['results']
    return data
def get_location_names()->list:
    return[i['name']for i in get_list_location()]

def get_location_data(name:str)->dict:
    locations={i['name']:i['id']for i in get_list_location()}
    loc_id=locations[name]
    url =f'https://rickandmortyapi.com/api/location/{loc_id}'
    data=requests.get(url).json()
    return data

print(get_location_data('Anatomy Park'))
