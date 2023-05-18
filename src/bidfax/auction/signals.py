from django.db.models.signals import post_migrate
from django.dispatch.dispatcher import receiver

from celery import group

from bidfax.auction.tasks import save_car_brands, save_car_models


@receiver(post_migrate)
def run_saving_car_brands(sender, **kwargs):
    if sender.name == 'bidfax.auction':
        group(save_car_brands.s(), save_car_models.s()).apply_async()


@receiver(post_migrate)
def test(sender, **kwargs):
    if sender.name == 'bidfax.auction':
        print('Hello')
