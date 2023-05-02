from bidfax.auction.services.scraper import get_models_names
from bidfax.auction.models import Brand, Model


def car_save():
    for car in get_models_names():
        brand, created = Brand.objects.get_or_create(name=car['name'])
        Model.objects.bulk_create([Model(name=model, brand=brand) for model in car['models']])
