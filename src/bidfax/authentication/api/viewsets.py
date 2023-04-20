from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from bidfax.authentication.models import User
from bidfax.authentication.api.permissions import IsAdminOrIsSelf
from bidfax.authentication.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet, ):
    lookup_field = 'uid'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrIsSelf]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()
