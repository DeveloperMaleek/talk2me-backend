# Serializers for the Therapy Sessions API View


from dataclasses import fields
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from rest_framework import status
from rest_framework.response import Response

from django.utils.translation import gettext as _

from rest_framework import serializers
from core.models import AvailableTimeSlots

from core.models import TherapistBookingsSchedule

# from app.core.models import Sessions


class TherapistAvailableTimeSlotSerializers(serializers.ModelSerializer):
    # Serializer that creates and return the available time schedules for therapist

    class Meta:
        model = AvailableTimeSlots
        fields = ['time_slot']

        # def create_time_slot(request):
        #     # Schedule and return a therapist available schedules
        #     therapist_time_slot = AvailableTimeSlots.objects.create(
        #         booking=request.get.booking,
        #         time_slot=request.get.time_slot
        #     )

        #     if therapist_time_slot > 4:
        #         raise ValueError('Cannot select more than 4')

        #     return therapist_time_slot


class TherapistAvailablilitySerializer(serializers.ModelSerializer):
    # Serializer that creates and return therapy schedules for therapist

    # time_slots = TherapistAvailableTimeSlotSerializers(many=True)

    class Meta:
        model = TherapistBookingsSchedule
        fields = ['id', 'therapist_schedule_days',
                  'available_time_slot', 'therapist_number_of_sessions_per_day']

    def create(self, validated_data):
        # create and a therapist schedules
        return TherapistBookingsSchedule.objects.create_therapist_schedules(**validated_data)

        # return therapist_booking_date


# class TherapistAvailableTimeSlotSerializers(serializers.ModelSerializer):
#     # Serializer that creates and return the available time schedules for therapist

#     class Meta:
#         model = AvailableTimeSlots
#         fields = ['booking', 'first_time_slot', 'second_time_slot',
#                   'third_time_slot', 'fourth_time_slot']

#     def create_therapist_schedules(request):
#         # Schedule and return a therapist available schedules
#         therapist_booking_date = TherapistBookingsSchedule.objects.create(
#             user=request.get.user,
#             sessions_number=request.get.therapist_number_of_sessions_per_day,
#             available_days_of_the_week=request.get.therapist_schedule_days,
#         )

#         if therapist_booking_date.sessions_number == 1:
#             AvailableTimeSlots.objects.create(
#                 booking=therapist_booking_date,
#                 first_time_slot=request.get.first_time_slot
#             )
#         elif therapist_booking_date.sessions_number == 2:
#             AvailableTimeSlots.objects.create(
#                 booking=therapist_booking_date,
#                 first_time_slot=request.get.first_time_slot,
#                 second_time_slot=request.get.second_time_slot
#             )
#         elif therapist_booking_date.sessions_number == 3:
#             AvailableTimeSlots.objects.create(
#                 booking=therapist_booking_date,
#                 first_time_slot=request.get.first_time_slot,
#                 second_time_slot=request.get.second_time_slot,
#                 third_time_slot=request.get.third_time_slot,
#             )
#         else:
#             AvailableTimeSlots.objects.create(
#                 booking=therapist_booking_date,
#                 first_time_slot=request.get.first_time_slot,
#                 second_time_slot=request.get.second_time_slot,
#                 third_time_slot=request.get.third_time_slot,
#                 fourth_time_slot=request.get.fourth_time_slot,
#             )

#         return AvailableTimeSlots
