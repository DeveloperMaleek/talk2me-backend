from django.urls import path
from agora import views


urlpatterns = [
    path('agora/token/', views.AgoraToken.as_view(), name='agora-token'),
]
