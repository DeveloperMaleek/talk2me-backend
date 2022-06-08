# Serializers for the user API View


from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from rest_framework import status
from rest_framework.response import Response

from django.utils.translation import gettext as _

from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    # Serializers for user create account.

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'first_name']
        extra_kwargs = {'password': {'min_length': 5}}

    # Create and return a user with encrypted password.

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    # def validate(self, validated_data):
    #     # Validate and authentcate the user.
    #     email = validated_data.get('email')
    #     password = validated_data.get('password')
    #     user = authenticate(
    #         request=self.context.get('request'),
    #         username=email,
    #         password=password,
    #     )
    #     if not user:
    #         msg = _('Unable to authenticate with provided credentials')
    #         raise serializers.ValidationError(msg, code='authorization')

    #     validated_data['user'] = user
    #     return validated_data


class UserUpdateSerializer(serializers.ModelSerializer):
    # Serializer for user update account.

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password',
                  'first_name', 'last_name', 'is_therapist', 'is_user_anonymous', 'profile_image_url', 'profile_cover_image_url', 'anonymous_display_name', 'anonymous_profile_image_url', 'user_bio', 'user_social_urls', 'user_goals', ]
        read_only_fields = ['id']
        extra_kwargs = {'password': {'min_length': 5}}

    def update(self, instance, validated_data):
        # Update and return user.
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


# class UserAnonymousProfile(serializers.ModelSerializer):
#     # Serializers for setting user's profile to anonymous

#     class Meta:
#         model = get_user_model()
#         field = ['is_user_anonymous', 'anonymous_display_name',
#                  'anonymous_profile_image_url', ]

#     def set_to_anonymous(self, validated_data):
#         # Create and return an anonymous user
#         return get_user_model().objects.set_profile_to_anonymous(**validated_data)


class UserSetupSerializer(serializers.ModelSerializer):
    # Serializers for user to setup account process two

    class Meta:
        model = get_user_model()
        fields = ['id', 'user_emotions', 'user_emotions_triggers',
                  'user_goals', ]

    def setup_two(self, validated_data):
        # setup and return four account setup processes for users.
        return get_user_model().objects.setup_account(**validated_data)


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
