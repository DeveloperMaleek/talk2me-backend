# Serializers for the user API View

import email
from django.contrib.auth import (
    get_user_model,
    authenticate,
)

from django.utils.translation import gettext as _

from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    # Serializers for user create account.

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', ]
        extra_kwargs = {'password': {'min_length': 5}}

    def create(self, validated_data):
        # Create and return a user with encrypted password.
        return get_user_model().objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    # Serializer for user update account.

    class Meta:
        model = get_user_model()
        fields = ['email', 'password',
                  'first_name', 'last_name', ]
        extra_kwargs = {'password': {'min_length': 5}}

    def update(self, instance, validated_data):
        # Update and return user.
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserSetupOneSerializer(serializers.ModelSerializer):
    # Serializers for user to setup account process one.

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

    def setup(self, validated_data):
        # setup and return first name and last name for new user.
        return get_user_model().objects.setup_account_one(**validated_data)


class UserSetupTwoSerializer(serializers.ModelSerializer):
    # Serializers for user to setup account process two

    class Meta:
        model = get_user_model()
        fields = ['user_emotions']

    def setup_two(self, validated_data):
        # setup and return four account setup processes for users.
        return get_user_model().objects.setup_account_two(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    # Serializers for the user Auth Token
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        # Validate and authentcate the user.
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
