import requests
# from img import get_img

def get_info()->list:
    url='https://back.detox.today/api/v1/products/'
    res=requests.get(url).json()
    return res
# print(get_info())
def get_image()->list:
    url='https://back.detox.today/api/v1/image/'
    data=requests.get(url).json()
    return data

def get_info_title()->list:
    return[i['title'] for i in get_info()]
# print(get_info_title())


def get_info_data(title: str)->dict:
    names={i['title']:i['id']for i in get_info()} 
    url=f'https://back.detox.today/api/v1/products/{names[title]}'
    data=requests.get(url).json()
    return data

def get_img_for(idd:str)->dict:
    image={i['title']:i['id'] for i in get_image()}
    url=f'https://back.detox.today/api/v1/image/{image[idd]}'
    data=requests.get(url).json()
    return data['img']

def det_info_text(idd,title:str)->str:
    try:
        data=get_info_data(title)
        img=get_img_for(idd)
        text=f'''\nОписание: {data['description']}\nЦена: {data['price']}\n{img}'''
        return text
    except Exception:
        return 'oops!'
# print(det_info_text('Программа «Бодрость» 1 день'))