# User models for Talk2me

from rest_framework import status
from rest_framework.response import Response
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.conf import settings

from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    # Manager for user in the system

    def create_user(self, email, password=None, **extra_fields):
        # Create, save and return a new user.
        if not email:
            raise ValueError('User must have email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def setup_account(self, request):
        # Update and return user's account setup two
        user = Talk2meUser.objects.get(email=request.user.email)
        user.user_emotions = 'user_emotions'
        user.user_emotions_triggers = 'user_emotions_triggers'
        user.user_goals = 'user_goals'

        user.save(using=self._db)

        return user

    # def set_profile_to_anonymous(self, request):
    #     # Set user's profile to anonymous
    #     new_user = Talk2meUser.objects.get(email=request.user.email)
    #     new_user.is_user_anonymous = True
    #     new_user.anonymous_profile_image_url = 'anonymous_profile_image_url'
    #     new_user.anonymous_display_name = 'anonymous_display_name'

    #     new_user.save(using=self._db)

    #     return new_user

    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserEmotions(models.Model):
    # Emotions of users in the system
    emotions = models.CharField(max_length=15)

    def __str__(self):
        return self.emotions


class UserEmotionsTriggers(models.Model):
    # Factors that triggers emotion of users in the system
    triggers = models.CharField(max_length=30)

    def __str__(self):
        return self.triggers


class UserGoals(models.Model):
    # Goals of users in the system
    goals = models.CharField(max_length=30)

    def __str__(self):
        return self.goals


class UserCurrentFEmotionalState(models.Model):
    # Current emotional state of users in the system
    current_emotional_state = models.CharField(max_length=30)

    def __str__(self):
        return self.current_emotional_state


class UserAnonymousDisplayImage(models.Model):
    # Default anonymous display images of users in the system
    anonymous_display_image = models.CharField(max_length=255)

    def __str__(self):
        return self.anonymous_display_image


class UserProfileCoverImage(models.Model):
    # Default profile cover images of users in the system
    profile_cover_image = models.CharField(
        max_length=255,)

    def __str__(self):
        return self.profile_cover_image


class UserSocialUrls(models.Model):
    # Social links of users in the system
    facebook = models.CharField(max_length=255, default='', )
    linkedin = models.CharField(max_length=255, default='', )
    twitter = models.CharField(max_length=255, default='', )

    def __str__(self):
        return "%s %s %s" % (self.facebook, self.linkedin, self.twitter)


class Talk2meUser(AbstractBaseUser, PermissionsMixin):

    # User in the system
    email = models.EmailField(
        verbose_name="Email address",
        unique=True,
        max_length=255
    )
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    is_active = models.BooleanField(default=True)
    is_user_anonymous = models.BooleanField(default=False)
    is_therapist = models.BooleanField(default=False)
    profile_image_url = models.TextField(blank=True)
    profile_cover_image_url = models.ForeignKey(
        UserProfileCoverImage, null=True, on_delete=models.CASCADE)
    anonymous_display_name = models.CharField(max_length=255, blank=True)
    anonymous_profile_image_url = models.ForeignKey(
        UserAnonymousDisplayImage, null=True, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=300, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    user_emotions = models.ManyToManyField(UserEmotions)
    user_emotions_triggers = models.ManyToManyField(UserEmotionsTriggers)
    user_goals = models.ManyToManyField(UserGoals)
    user_current_emotional_state = models.ForeignKey(
        UserCurrentFEmotionalState, null=True, on_delete=models.CASCADE)
    user_social_urls = models.ForeignKey(
        UserSocialUrls, null=True, on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Organization(models.Model):
    # Organization a user is affliated with
    name_of_organization = models.CharField(max_length=255, unique=True)
    organization_access_code = models.IntegerField(
        unique=True, auto_created=True)
    organization_domain_url = models.URLField(max_length=255, unique=True)
    organization_contact_person = models.CharField(max_length=255)
    organization_contact_person_email = models.EmailField(
        unique=True, max_length=255)
    org_users = models.ForeignKey(
        Talk2meUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_organization


class TherapySessions(models.Model):
    # Sessions users will have in the system
    session_date = models.DateField()
    number_of_sessions = models.SmallIntegerField()
    session_users = models.ManyToManyField(Talk2meUser)


class AvailableTimeSlots(models.Model):
    # Time for the sessions for the users
    # booking = models.ForeignKey(
    #     TherapistBookingsSchedule, null=True, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=100)

    def __str__(self):
        return self.time_slot


class TherapistBookingsSchedule(models.Model):
    # Booking sessions for therapist
    DAY_CHOICES = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    therapist_number_of_sessions_per_day = models.IntegerField()
    therapist_schedule_days = models.CharField(
        choices=DAY_CHOICES, max_length=3)
    available_time_slot = models.ManyToManyField(AvailableTimeSlots)

    def create_therapist_schedules(self, request):
        # Schedule and return a therapist available schedules
        therapist_booking_date = TherapistBookingsSchedule.objects.get(
            user=request.get.user)
        therapist_booking_date.therapist_schedule_days = request.get.therapist_schedule_days,
        therapist_booking_date.available_time_slot = request.get.available_time_slot,
        therapist_booking_date.therapist_number_of_sessions_per_day = len(
            therapist_booking_date.available_time_slot),
        therapist_booking_date.save(using=self._db)

        return therapist_booking_date

    def __str__(self):
        return self.therapist_schedule_days
