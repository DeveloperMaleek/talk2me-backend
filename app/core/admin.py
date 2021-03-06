# Django admin customization

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
# from user import models


class UserAdmin(BaseUserAdmin):
    # Define the admin pages for users.
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name',
                'last_name', 'is_user_anonymous', 'anonymous_display_name', 'profile_image_url', 'anonymous_profile_image_url', 'user_bio', 'user_emotions',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'is_user_anonymous',
                'anonymous_display_name',
                'profile_image_url',
                'anonymous_profile_image_url',
                'user_bio',
                'user_emotions',
                'user_emotions_triggers',
                'user_goals',
                'user_current_emotional_state',
                'user_social_urls',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(models.Talk2meUser, UserAdmin)
admin.site.register(models.UserEmotions)
admin.site.register(models.UserEmotionsTriggers)
admin.site.register(models.UserGoals)
admin.site.register(models.UserCurrentFEmotionalState)
admin.site.register(models.UserAnonymousDisplayImage)
admin.site.register(models.UserProfileCoverImage)
admin.site.register(models.UserSocialUrls)
admin.site.register(models.Organization)
admin.site.register(models.TherapySessions)
admin.site.register(models.AvailableTimeSlots)
admin.site.register(models.TherapistBookingsSchedule)
