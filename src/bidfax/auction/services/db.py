from bidfax.auction.services.scraper import get_car_models_data
from bidfax.auction.models import Brand, Model


def car_models_save():
    for car in get_car_models_data():
        brand, created = Brand.objects.get_or_create(name=car['name'])
        Model.objects.bulk_create([Model(name=model, brand=brand) for model in car['models']])
