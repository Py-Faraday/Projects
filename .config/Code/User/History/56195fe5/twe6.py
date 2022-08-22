
from turtle import title
import requests
from pprint import pprint


def get_list_products() -> list:
    url = "https://back.detox.today/api/v1/products/"
    data = requests.get(url).json()
    return data


def get_product_names() -> list:
    return [i['title'] for i in get_list_products()]
pprint(get_product_names())


def _get_product_data(name: str) -> dict:
    product = {i['title']: i['id'] for i in get_list_products()}
    char_id = product[title]
    url = f"https://back.detox.today/api/v1/products/"
    data = requests.get(url).json()
    return data


# def get_character_text(name: str) -> str:
#     try:
#         data = _get_product_data(name)
#         text = f"""\
#         \nТип или подвид продукта: {data['discription']}\
#         \nИдентификатор продукта: {data['id']}\
#         \nИмя продукта: {data['title']}\
#         \nВид продукта: {data['']}\
#         \nТип или подвид продукта: {data['discription']}\
#         """
#         return text
#     except Exception:
#         return 'Продукт с таким названием не существует'
