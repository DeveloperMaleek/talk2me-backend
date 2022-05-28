
# Views for the user API.

from rest_framework import generics, authentication, permissions

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response

from user.serializers import (
    UserCreateSerializer,
    UserUpdateSerializer,
    UserSetupSerializer,
    # UserAnonymousProfile,
    # UserLoginSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    # Create a new user in the system.
    serializer_class = UserCreateSerializer


class CreateTokenView(ObtainAuthToken):
    # Create a new auth token for the user
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# class LoginUserView(generics.RetrieveAPIView):
#     # Login an existing user into the system
#     serializer_class = UserLoginSerializer
#     permission_classes = [permissions.IsAuthenticated]


class SetupUserView(generics.UpdateAPIView):
    # Setup account (feelings, triggers and goals) for a new user in the system.
    serializer_class = UserSetupSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Retrieve and return the authenticated user.
        return self.request.user


class ManageUserView(generics.RetrieveUpdateAPIView):
    # Manage the authenticated user.
    serializer_class = UserUpdateSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Retrieve and return the authenticated user.
        return self.request.user
