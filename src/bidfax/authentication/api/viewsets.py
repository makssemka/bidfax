from django.contrib.auth import get_user_model

from rest_framework import viewsets

from bidfax.authentication.models import Profile
from bidfax.authentication.api.serializers import UserSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
