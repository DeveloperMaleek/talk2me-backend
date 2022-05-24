# Url mappings for the user API

from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('setup/1/', views.SetupOneUserView.as_view(), name='setup-1'),
    path('setup/2/', views.SetupTwoUserView.as_view(), name='setup-2')
]
