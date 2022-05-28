# Url mappings for the user API

from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('login/', views.CreateTokenView.as_view(), name='login'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('account/setup/', views.SetupUserView.as_view(), name='account-setup'),
    # path('login/', views.LoginUserView.as_view(), name='login')
]
