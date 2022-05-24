
# Views for the user API.

from rest_framework import generics, authentication, permissions

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserCreateSerializer,
    UserUpdateSerializer,
    UserSetupOneSerializer,
    UserSetupTwoSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    # Create a new user in the system.
    serializer_class = UserCreateSerializer


class CreateTokenView(ObtainAuthToken):
    # Create a new auth token for the user
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class SetupOneUserView(generics.UpdateAPIView):
    # Setup account (personal information) for a new user in the system.
    serializer_class = UserSetupOneSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Retrieve and return the authenticated user.
        return self.request.user


class SetupTwoUserView(generics.UpdateAPIView):
    # Setup account (feelings and goals) for a new user in the system.
    serializer_class = UserSetupTwoSerializer
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
