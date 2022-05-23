# User models for Talk2me

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    # Manager for user in the system

    def create_user(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')
        user_bio = request.data.get('user_bio')

        if not email or email == '':
            raise ValueError('Please enter a valid email address')

        try:
            user: Talk2meUser.objects.get(email=self.normalize_email(email))
            if user:
                raise ValueError('Email address already exist')
        except Talk2meUser.DoesNotExist:
            new_user = Talk2meUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                user_bio=user_bio,
            )

            new_user.set_password(password)
            new_user.save(using=self._db)

            return new_user

    def create_superuser(self, email, password):
        # create and return a superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Talk2meUser(AbstractBaseUser, PermissionsMixin):
    # User in the system
    email = models.EmailField(
        verbose_name="Email address",
        unique=True,
        max_length=255
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_user_anonymous = models.BooleanField(default=False)
    anonymous_display_name = models.CharField(max_length=255, default="")
    profile_image_url = models.TextField(default='')
    anonymous_profile_image_url = models.TextField(default='')
    user_bio = models.TextField(max_length=300, default='')
    is_blocked = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


# from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager,
#     AbstractBaseUser,
#     PermissionsMixin)


# class UserManager(BaseUserManager):
#     # Manager for users.

#     def create_user(self, email, password=None, **extra_fields):
#         # create and return a user
#         if not email:
#             raise ValueError('User must have an email address')
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, password):
#         # create and return a superuser
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)

#         return user


# class User(AbstractBaseUser):
#     # users in the system
#     email = models.EmailField(max_length=255, unique=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255, default="")
#     is_anonymous = models.BooleanField(default=False)
#     anonymous_display_name = models.CharField(max_length=255, default="")
#     profile_image_url = models.TextField(default='')
#     anonymous_profile_image_url = models.TextField(default='')
#     user_bio = models.TextField(max_length=300, default='')
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()

# USERNAME_FIELD = 'email'


# class Talk2meUser(User):
#     # Users in the system
