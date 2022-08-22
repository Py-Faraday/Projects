
import requests
from pprint import pprint


def get_list_products() -> list:
    url = "https://back.detox.today/api/v1/products/"
    data = requests.get(url).json()
    return data


def get_product_names() -> list:
    return [i['title'] for i in get_list_products()]



def get_product_data(title: str) -> dict:
    product = {i['title']: i['id'] for i in get_list_products()}
    product_id = product[title]
    url = f"https://back.detox.today/api/v1/products/{product_id}"
    data = requests.get(url).json()
    return data


def get_product_text(title: str) -> str:
    try:
        data = get_product_data(title)
        text = f"""\
        \nТип или подвид продукта: {data['discription']}\
        \nИдентификатор продукта: {data['id']}\
        \nИмя продукта: {data['title']}\
        \nЦена продукта: {data['price']}\
        """
        return text
    except Exception:
        return 'Продукт с таким названием не существует'
