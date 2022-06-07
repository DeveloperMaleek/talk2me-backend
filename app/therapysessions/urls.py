from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from therapysessions import views

app_name = 'therapysessions'

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'therapistavailableschedules',
#                 views.ScheduleTherapistSessionsViews, basename="therapist-available-schedules")

# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('create/schedule', views.ScheduleTherapistSessionsViews.as_view(),
         name='create-therapy-schedules'),
]
