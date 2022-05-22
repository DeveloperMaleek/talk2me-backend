# Serializers for the user API View

from pyexpat import model
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # Serializers for user objects.

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'users_name']
        extra_kwargs = {'password': {'write-only': True, 'min_length': 5}}

    def create(self, validated_data):
        # Create and return a user with encrypted password.
        return get_user_model().objects.create_user(**validated_data)
