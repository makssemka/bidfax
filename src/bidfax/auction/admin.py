from django.contrib import admin

from bidfax.auction.models import Brand, Model, Condition, Spec, Information, Auction, Lot


admin.site.register([Brand, Model, Condition, Spec, Information, Auction, Lot])
# admin.site.register(Model)
# admin.site.register(Condition)
# admin.site.register(Spec)
# admin.site.register(Information)
# admin.site.register(Auction)
# admin.site.register(Lot)

# Register your models here.
