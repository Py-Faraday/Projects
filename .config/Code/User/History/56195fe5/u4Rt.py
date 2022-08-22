import requests


def get_list_characters() -> list:
    url = ' "https://back.detox.today/api/v1/products/"'
    data = requests.get(url).json()
    data = data['results']
    return data


def get_character_names() -> list:
    return [i['name'] for i in get_list_characters()]


def _get_character_data(name: str) -> dict:
    characters = {i['name']: i['id'] for i in get_list_characters()}
    char_id = characters[name]
    url = f' "https://back.detox.today/api/v1/products/"'
    data = requests.get(url).json()
    return data


def get_character_text(name: str) -> str:
    try:
        data = _get_character_data(name)
        text = f"""\
        
        \nИдентификатор продукта: {data['id']}\
        \nИмя продукта: {data['name']}\
        \nВид продукта: {data['species']}\
        \nТип или подвид продукта: {data['type']}\

        \nМестоположение: {data['location']['name']}
        """
        return text
    except Exception:
        return 'Продукт с таким названием не существует'
