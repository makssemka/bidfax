from rest_framework import serializers

from bidfax.auction.models import Brand, Model, Condition, Spec, Information, Auction, Lot


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = 'name'


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = ('name', 'brand')


class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = '__all__'


class SpecSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spec
        fields = '__all__'


class InformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = '__all__'


class AuctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auction
        fields = '__all__'


class LotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        fields = '__all__'
