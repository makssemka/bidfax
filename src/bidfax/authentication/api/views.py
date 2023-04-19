from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.response import Response

from bidfax.authentication.models import Profile
from bidfax.authentication.api.serializers import ProfileSerializer, AuthTokenSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class TokenView(ObtainAuthToken):
    serializers_class = AuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

        def post(self, request, *args, **kwargs):
            token = super().post(request, *args, **kwargs)
            return Response({
                'token': token,
                'user': self.get_serializer().validated_data['user']
            })
