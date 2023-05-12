import time

import requests
from requests import Session
import js2py
from bs4 import BeautifulSoup
import subprocess

proxies = {
    'http': 'http://127.0.0.1:8005',
    'https': 'http://127.0.0.1:8005'
}

headers = {
    'Host': 'bidfax.info',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.71 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "*",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0"
}


def _get_fort() -> str:
    """Return required FORT cookie value for subsequent successful requests."""
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url='https://bidfax.info/', proxies=proxies)
    script = BeautifulSoup(response.text, 'html.parser').find_all('script')[1].get_text()
    slowAES = session.get('https://bidfax.info/aes.min.js', proxies=proxies).text
    jslogic = script.split('document.cookie="')[0]
    FORT: str = js2py.eval_js(slowAES + jslogic + " toHex(slowAES.decrypt(c,2,a,b));")
    return FORT


def _get_session() -> Session:
    """Return bidfax session with required headers and cookies."""
    session = requests.Session()
    session.headers.update(headers)
    try:
        session.cookies.update({'FORT': _get_fort()})
    except requests.exceptions.RequestException as e:
        print('Ошибка при выполнении запроса:', e)
        print('Перезапуск контейнера...')
        restart_container()
        time.sleep(2)
        session.cookies.update({'FORT': _get_fort()})
    return session


def restart_container():
    try:
        subprocess.run(["docker", "restart", "opera-proxy"], check=True)
        print("Контейнер успешно перезапущен.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при перезапуске контейнера: {e}")
