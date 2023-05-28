import re
import requests
from typing import Any, Optional

import js2py
from bs4 import BeautifulSoup


class Scraper:

    _response: Optional[requests.Response] = None

    car_brands: Optional[list] = None
    car_models: Optional[list] = None
    car_lots: Optional[dict] = None

    def __init__(self,
                 url: str,
                 session: Optional[requests.Session] = None,
                 proxies: Optional[dict] = None,
                 cookies: Optional[dict] = None,
                 headers: Optional[dict] = None):
        self.url = url
        self.session = session or requests.Session()
        self.proxies = proxies
        self.cookies = cookies
        self.headers = headers

    def connect(self):
        self._prepare_connect()
        self._response = self.session.get(url=self.url, proxies=self.proxies, headers=self.headers)
        self._response.encoding = 'utf-8'
        return self._response

    def _prepare_connect(self):
        init_response = self.session.get(url=self.url, proxies=self.proxies, headers=self.headers)
        script = self.parse_response(init_response.text, 'script')
        return self.set_cookies(FORT=self._get_jslogic(script))

    def _get_jslogic(self, script):
        slowAES = self.session.get('https://bidfax.info/aes.min.js', proxies=self.proxies).text
        jslogic = script.split('document.cookie="')[0]
        return js2py.eval_js(slowAES + jslogic + " toHex(slowAES.decrypt(c,2,a,b));")

    def set_cookies(self, **kwargs):
        self.cookies = {f'{k}': v for k, v in kwargs.items()}
        return self.session.cookies.update({f'{k}': v for k, v in kwargs.items()})

    def get_car_brands(self):
        soup = BeautifulSoup(self._response.text, 'lxml')
        self.car_brands = [(brand_data.text, brand_data.get('href'))
                           for brand_data in soup.find('div', class_='drop-menu-main-sub').find_all('a')]
        return self.car_brands

    def get_car_models(self):
        self.car_models = []
        for brand in self.car_brands:
            print(brand)
            car_model_page = self.session.get(brand[1], proxies=self.proxies, headers=self.headers)
            print(car_model_page.text)
            soup = BeautifulSoup(car_model_page.text, 'lxml')
            self.car_models.append({'name': brand[0],
                                    'models': [car_model.text for car_model in
                                   soup.find_all('div', class_='drop-menu-main-sub')[1].find_all('a')]})
        return self.car_models

    def get_car_lots(self):
        car_urls_per_page = []
        for brand in self.car_brands:
            urls_per_page = self._parse_list_car_urls(self.session.get(url=brand[1],
                                                                       proxies=self.proxies,
                                                                       headers=self.headers).text
                                                      )
            car_urls_per_page += urls_per_page
        return self._get_detail_car_data(car_urls_per_page[:5])

    @staticmethod
    def parse_response(response, tag_name) -> Any:
        element = BeautifulSoup(response, 'html.parser').find_all('script')[1].get_text()
        return element

    @staticmethod
    def _parse_list_car_urls(detail_car_data: str) -> list:
        soup = BeautifulSoup(detail_car_data, 'lxml')
        cars = soup.find_all('div', class_='thumbnail offer')
        if not cars:
            print(cars)

        def find_a(car):
            try:
                return car.find('a').get('href')
            except AttributeError:
                pass

        return [find_a(car) for car in cars if find_a(car)]

    def _get_detail_car_data(self, car_urls: list) -> list:
        return [self._parse_detail_car_data(self.session.get(
            url=url, proxies=self.proxies, headers=self.headers).text
                                       ) for url in car_urls]

    def _parse_detail_car_data(self, detail_car_data):
        soup = BeautifulSoup(detail_car_data, 'lxml')
        car_info = {info.text.split(':')[0]: info.text.split(':')[1].strip().replace(u'\xa0', u' ') for info in
                    soup.find('div', id='aside').find_all('p')
                    if not re.match('Ціна ремонту', info.text)}
        car_info.update(self._get_image(soup))
        car_info.update(self._get_brand_and_model_name(soup))
        car_info.update(self._get_car_price(soup))
        car_info.update(self._get_repair_price(soup))
        return car_info

    def _get_image(self, soup: BeautifulSoup) -> dict:
        img_url = soup.find('div', class_='col-xs-12 col-md-12').find('div', class_='full-screens').find('img').get(
            'src')
        image = self.session.get(
            url=self.url + img_url,
            proxies=self.proxies, headers=self.headers,
            cookies=self.cookies
        )
        return {'image': image.content}

    @staticmethod
    def _get_brand_and_model_name(soup: BeautifulSoup) -> dict:
        brand = soup.find_all('div', class_='demo')[0].find('span').text
        model = soup.find_all('div', class_='demo')[1].find('span').text
        return {'BrandName': brand, 'ModelName': model}

    @staticmethod
    def _get_car_price(soup: BeautifulSoup) -> dict:
        return {'BID': soup.find('div', class_='bidfax-price').find('span').text}

    @staticmethod
    def _get_repair_price(soup: BeautifulSoup) -> dict:
        return {info.text.split('≈')[0].strip().replace(u'\xa0',
                                                        u' '): info.text.split('≈')[1].strip().replace(u'\xa0',
                                                                                                       u' ')
                for info in soup.find('div', id='aside').find_all('p') if re.match('Ціна ремонту', info.text)}
