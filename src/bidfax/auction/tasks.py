from io import BytesIO

from celery import shared_task
from django.core.files.images import ImageFile

from bidfax.auction.models import Brand, CarModel, Auction, Spec, Information, Condition, Lot
from bidfax.auction.services.connection import scraper


@shared_task
def save_car_brands():
    for car_brand in scraper.get_car_brands():
        brand, created = Brand.objects.get_or_create(name=car_brand[0])


@shared_task
def save_car_models():
    for car_model in scraper.get_car_models():
        brand, created = Brand.objects.get_or_create(name=car_model['name'])
        CarModel.objects.bulk_create(map(lambda name: CarModel(brand_id=brand.pk, name=name), car_model['models']))


@shared_task
def save_car_lots():
    for car_lot in scraper.get_car_lots():
        auction, created = Auction.objects.get_or_create(auction_name=car_lot['Аукціон'],
                                                         documents=car_lot['Документи'],
                                                         location=car_lot['Місце продажу'], seller=car_lot['Продавець']
                                                         )
        spec, created = Spec.objects.get_or_create(transmission=car_lot['Коробка передач'], drive=car_lot['Привід'],
                                                   engine=car_lot['Двигун'], fuel=car_lot['Паливо'])
        information, created = Information.objects.get_or_create(lot_number=car_lot['Номер лоту'],
                                                                 estimate_coast=car_lot['Оціночна вартість'],
                                                                 repair_price=car_lot['Ціна ремонту'],
                                                                 note=car_lot['Примітка'])
        condition, created = Condition.objects.get_or_create(primary_damage=car_lot['Основне ушкодження'],
                                                             secondary_damage=car_lot['Другорядне пошкодження'],
                                                             condition=car_lot['Стан']
                                                             )
        brand = Brand.objects.get(name=car_lot['BrandName'].split('▼')[0].strip())
        car_model = CarModel.objects.get(brand=brand, name=car_lot['ModelName'].split('▼')[0])
        image_data = car_lot['image']
        temp_file = BytesIO()
        temp_file.write(image_data)
        temp_file.seek(0)
        image = ImageFile(temp_file, name=f'{car_lot["VIN"]}.jpeg')
        Lot.objects.create(year=car_lot['Рік випуску'],
                           color=car_lot['Колір кузова'],
                           mileage=car_lot['Пробіг'].split()[0],
                           vin=car_lot['VIN'],
                           sale_date=car_lot['Дата продажу'],
                           bid=car_lot['BID'],
                           image=image,
                           condition=condition,
                           spec=spec,
                           information=information,
                           auction=auction,
                           car_model=car_model
                           )
