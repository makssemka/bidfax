from bidfax.auction.services.scraper import get_car_models_data
from bidfax.auction.models import Brand, CarModel


def car_models_save():
    for car in get_car_models_data():
        brand, created = Brand.objects.get_or_create(name=car['name'])
        CarModel.objects.bulk_create([CarModel(name=model, brand=brand) for model in car['models']])
