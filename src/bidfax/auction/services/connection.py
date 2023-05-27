from bidfax.auction.services.scraper import Scraper

proxies = {
    'http': 'http://138.68.76.255:8000',
    'https': 'http://138.68.76.255:8000'
}

# proxies = {
#     'http': 'http://127.0.0.1:8005',
#     'https': 'http://127.0.0.1:8005'
# }

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

scraper = Scraper(url='https://bidfax.info/', proxies=proxies, headers=headers)
scraper.connect()
