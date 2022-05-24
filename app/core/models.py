# User models for Talk2me
from email.policy import default
from random import choices
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

from django.utils.translation import gettext_lazy as _

from multiselectfield import MultiSelectField


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

    def setup_account_one(self, request):
        # Update and return user's first name and last name
        new_user = Talk2meUser.objects.get(email=request.user.email)
        new_user.first_name = 'first_name'
        new_user.last_name = 'last_name'

        new_user.save(using=self._db)

        return new_user

    def setup_account_two(self, request):
        # Update and return user's account setup two
        new_user = Talk2meUser.objects.get(email=request.user.email)
        new_user.user_emotions = 'user_emotions'

        new_user.save(using=self._db)

        return new_user

    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Emotions of users in the system
EMOTIONS = (
    (1, 'hopeful'),
    (2, 'Excited'),
    (3, 'Sad'),
    (4, 'Anxious'),
    (5, 'Frustrated'),
    (6, 'Withdrawn'),
    (7, 'Stressed'),
    (8, 'Scared'),
    (9, 'Lonely'),
    (10, 'Happy'),
    (11, 'Indifferent'),
    (12, 'Angry'),
    (13, 'No feelings'),
)


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
    anonymous_display_name = models.CharField(max_length=255, default="")
    profile_image_url = models.TextField(default='')
    anonymous_profile_image_url = models.TextField(default='')
    user_bio = models.TextField(max_length=300, default='')
    # is_blocked = models.BooleanField(default=False)
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_modified = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    user_emotions = MultiSelectField(choices=EMOTIONS, default=13)

    objects = UserManager()

    USERNAME_FIELD = 'email'
