from django.db import IntegrityError
# from sqlite3 import IntegrityError

from bidfax.auction.services.scraper import get_car_models_data, get_car_data
from bidfax.auction.models import Brand, CarModel, Auction, Spec, Information, Lot, Condition


def car_models_save():
    for car in get_car_models_data():
        brand, created = Brand.objects.get_or_create(name=car['name'])
        CarModel.objects.bulk_create([CarModel(name=model, brand=brand) for model in car['models']])


def save_lots():
    car_data = get_car_data()
    for cd in car_data:
        auction, created = Auction.objects.get_or_create(auction_name=cd['Аукціон'], documents=cd['Документи'],
                                                         location=cd['Місце продажу'], seller=cd['Продавець'])
        spec, created = Spec.objects.get_or_create(transmission=cd['Коробка передач'], drive=cd['Привід'],
                                                   engine=cd['Двигун'], fuel=cd['Паливо'])
        print(spec)
        information, created = Information.objects.get_or_create(lot_number=cd['Номер лоту'],
                                                                 estimate_coast=cd['Оціночна вартість'],
                                                                 repair_price=cd['Ціна ремонту'],
                                                                 note=cd['Примітка'])
        condition, created = Condition.objects.get_or_create(primary_damage=cd['Основне ушкодження'],
                                                             secondary_damage=cd['Другорядне пошкодження'],
                                                             condition=cd['Стан']
                                                             )
        brand = Brand.objects.get(name=cd['BrandName'].split('▼')[0].strip())
        car_model = CarModel.objects.get(brand=brand, name=cd['ModelName'].split('▼')[0])
        try:
            Lot.objects.create(year=cd['Рік випуску'],
                               color=cd['Колір кузова'],
                               mileage=cd['Пробіг'].split()[0],
                               vin=cd['VIN'],
                               sale_date=cd['Дата продажу'],
                               bid=cd['BID'],
                               image=cd['image'],
                               condition=condition,
                               spec=spec,
                               information=information,
                               auction=auction,
                               car_model=car_model
                               )
        except IntegrityError:
            pass
