from rest_framework import generics
from rest_framework.permissions import AllowAny

from bidfax.auction.models import Brand, CarModel, Lot
from bidfax.auction.api.serializers import BrandSerializer, CarModelSerializer, LotSerializer


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (AllowAny, )


class BrandDetailView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'pk'


class ModelView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (AllowAny, )


class ModelDetailView(generics.RetrieveAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'pk'


class LotView(generics.ListAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_classes = (AllowAny, )
