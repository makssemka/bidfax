from celery import shared_task

from bidfax.auction.models import Brand, CarModel
from bidfax.auction.services.scraper import get_car_brands, get_car_models


@shared_task
def save_car_brands():
    for brand in get_car_brands():
        brand, created = Brand.objects.get_or_create(name=brand[0])


@shared_task
def save_car_models():
    car_models = get_car_models()
    print(car_models)
    for car in car_models:
        brand = Brand.objects.get(name=car['name'])
        try:
            CarModel.objects.bulk_create(
                [CarModel(name=carmodel_name, brand_id=brand.pk) for carmodel_name in car['models']]
            )
        except Exception:
            pass
