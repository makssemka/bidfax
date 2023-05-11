from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from bidfax.auction.models import Brand
from bidfax.auction.api.serializers import BrandSerializer
from bidfax.auction.services.db import car_models_save, save_lots


class BrandListView(generics.ListAPIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        car_models_save()
        save_lots()
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
