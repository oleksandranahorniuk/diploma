import requests
from bs4 import BeautifulSoup
url = 'https://comfy.ua/ua/bonus/?gad_source=1&gclid=Cj0KCQiAtOmsBhCnARIsAGPa5ya2GHrWLHvxPWnw9LSf_CILsRhhMqGaXpFcTFCw8Dfrc3fHNZQSZCwaArWGEALw_wcB'

# Отримуємо вміст сторінки
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Знаходимо всі елементи, що містять ціни
    prices = soup.find_all(class_='product-price')

    # Виводимо знайдені ціни
    for price in prices:
        print(price.text)
else:
    print('Не вдалося отримати доступ до сторінки')

def get_product_prices(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Виконуємо HTTP-запит до сторінки
    response = requests.get(url, headers=headers)

 if response.status_code == 200:
 # Використовуємо BeautifulSoup для парсингу HTML
 soup = BeautifulSoup(response.text, 'html.parser')

 # Задаємо CSS-селектор для елементів, які містять ціни
 price_elements = soup.select('.product-price')

 # Витягуємо ціни та виводимо їх
 prices = [element.text.strip() for element in price_elements]
 for i, price in enumerate(prices, start=1):
 print(f'Product {i} Price: {price}')
 else:
 print(f'Failed to retrieve the page. Status Code: {response.status_code}')

# Приклад виклику функції з URL конкретного сайту
url_to_parse = 'https://example.com/products'
get_product_prices(url_to_parse)
