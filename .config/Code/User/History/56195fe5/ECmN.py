from itertools import product
import requests


def get_list_products() -> list:
    url = "https://back.detox.today/api/v1/products/"
    data = requests.get(url).json()
    return data


def get_product_names() -> list:
    return [i['name'] for i in get_list_products()]


def _get_product_data(name: str) -> dict:
    product = {i['name']: i['id'] for i in get_list_products()}
    char_id = product[name]
    url = f"https://back.detox.today/api/v1/products/"
    data = requests.get(url).json()
    return data


def get_character_text(name: str) -> str:
    try:
        data = _get_product_data(name)
        text = f"""\
        
        \nИдентификатор продукта: {data['id']}\
        \nИмя продукта: {data['name']}\
        \nВид продукта: {data['species']}\
        \nТип или подвид продукта: {data['type']}\
        """
        return text
    except Exception:
        return 'Продукт с таким названием не существует'
