from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets

from bidfax.authentication.models import User
from bidfax.authentication.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet, ):
    lookup_field = 'uid'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
