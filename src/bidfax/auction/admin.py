from django.contrib import admin

from bidfax.auction.models import Brand, CarModel, Condition, Spec, Information, Auction, Lot, Image


admin.site.register([Brand, CarModel, Condition, Spec, Information, Auction, Lot, Image])
gi