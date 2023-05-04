from rest_framework import serializers

from bidfax.auction.models import Brand, CarModel, Condition, Spec, Information, Auction, Lot


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('name', 'pk')


class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ('name', 'brand')


class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = ('primary_damage', 'secondary_damage', 'condition')


class SpecSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spec
        fields = ('transmission', 'drive', 'engine', 'fuel')


class InformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = ('lot_number', 'estimate_coast', 'repair_price', 'note')


class AuctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auction
        fields = ('auction_name', 'documents', 'location', 'seller')


class LotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        fields = ('color', 'mileage', 'vin', 'sale_date', 'bid', 'image',
                  'condition', 'spec', 'information', 'auction', 'car_model')
