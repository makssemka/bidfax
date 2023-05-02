from django.contrib import admin

from bidfax.auction.models import Brand, Model, Condition, Spec, Information, Auction, Lot


admin.site.register([Brand, Model, Condition, Spec, Information, Auction, Lot])
