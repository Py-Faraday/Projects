import requests
def get_list_episode() -> list:
    url = 'https://rickandmortyapi.com/api/episode'
    r =requests.get(url)
    data = r.json()['results']
    return data

def episode_names() -> list:
    data = []
    for i in get_list_episode():
        data.append(i['name'])
    return data

def get_episode_data(name:str) -> dict:
    episode={i['name']:i['id'] for i in get_list_episode()}
    epi_id=episode[name]
    url = f"https://rickandmortyapi.com/api/episode/{epi_id}"
    data = requests.get(url).json()
    return data

def parso_data(name: str) -> str:
    data = get_episode_data(name)
    text = f"""
идентификатор: {data[ 'id' ]}
имя: {data['name']}
дата : {data['air_date']}
эпизод: {data['episode']}
разрешение: {name}
"""
    return text