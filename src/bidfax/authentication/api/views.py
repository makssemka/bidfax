from rest_framework import generics

from bidfax.authentication.models import Profile
from bidfax.authentication.api.serializers import ProfileSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
