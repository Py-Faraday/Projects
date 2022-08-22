import requests


def get_epizody()->list:
    url='https://rickandmortyapi.com/api/episode'
    r =requests.get(url)

    data=r.json()['results']
    return data
def get_epizody()->list:
    return[i['name']for i in get_epizody()]

def get_epizody(name:str)->dict:
    epizods={i['name']:i['id']for i in get_epizody()}
    epiz_id=epizods[name]
    url =f'https://rickandmortyapi.com/api/episode/{epiz_id}'
    data=requests.get(url).json()
    return data

def nons_data(name:str)->str:
    data=get_epizody(name)
    residents=data['residents']
    r=[]
    for url in residents:
        c=requests.get(url).json()
        name=c['name']
        r.append(name)
    text=f"""
id:{data['id']}
name:{data['name']}
type:{data['type']}
dimension:{data['dimension']}
created:{data['created']}
residents:{r}
"""
    return text
