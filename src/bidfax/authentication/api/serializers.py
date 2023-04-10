from rest_framework import serializers

from bidfax.authentication.models import User, Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'uid')
        extra_kwargs = {
            'uid': {
                'read_only': True
            },
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        pass


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'avatar', 'user')
