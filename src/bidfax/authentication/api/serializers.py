from django.contrib.auth import authenticate

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
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'avatar', 'user')


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label='Email', write_only=True)
    password = serializers.CharField(label='Password', trim_whitespace=True, write_only=True)
    token = serializers.CharField(label='Token', read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials', code='authorization')

        else:
            raise serializers.ValidationError('Must include "email" and "password".', code='authorization')

        attrs['user'] = user
        return user
