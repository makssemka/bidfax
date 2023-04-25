from rest_framework import generics
from rest_framework import views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from bidfax.authentication.models import Profile
from bidfax.authentication.api.permissions import IsProfileOwner
from bidfax.authentication.api.serializers import ProfileSerializer, AuthTokenSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    lookup_field = 'user__uid'
    lookup_url_kwarg = 'uid'
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsProfileOwner, )
    parser_classes = (MultiPartParser, FormParser)


class TokenCreateView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

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
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': serializer.validated_data['user'].email
        })


class TokenDeleteView(views.APIView):

    def post(self, request, *args, **kwargs):
        Token.objects.filter(user=request.user).delete()
        return Response()
