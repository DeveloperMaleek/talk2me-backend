# Therapy Session API Viewset


from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from therapysessions.serializers import TherapistAvailablilitySerializer
from core.models import TherapistBookingsSchedule


class ScheduleTherapistSessionsViews(generics.CreateAPIView):
    serializer_class = TherapistAvailablilitySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Retrieve and return the authenticated user.
        return self.request.TherapistBookingsSchedule