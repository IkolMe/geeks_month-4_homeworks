import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

url = 'https://cars.kg/offers/?vendor=57fa24ee2860c45a2a2c08b0'
HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7',
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 '
                  'Safari/537.36'
}


@csrf_exempt
def get_html(url, params=''):
    request_cars = requests.get(url, headers=HEADER, params=params)
    return request_cars


@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='catalog-list-item')
    cars = []
    for i in items:
        cars.append({
            'title': i.find('span', class_='catalog-item_caption').get_text(),
            'description': i.find('span', class_='catalog-item-descr').get_text(),
            'price': i.find('span', class_='catalog-item-price').get_text(),
            'image': url + i.find('span', class_='catalog-item-cover').find('img').get('src')
        })
    return cars


@csrf_exempt
def parser_cars():
    html = get_html(url)
    if html.status_code == 200:
        all_cars = []
        for page in range(0, 1):
            html = get_html(f'https://cars.kg/offers/?vendor=57fa24ee2860c45a2a2c08b0', params=page)
            all_cars.extend(get_data(html.text))
        return all_cars
    else:
        raise Exception('ERROR IN PARSE')

