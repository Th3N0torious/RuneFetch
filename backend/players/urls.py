from django.urls import path
from .views import test_api, get_player

urlpatterns = [
    path('test/', test_api),
    path('player/<str:username>/', get_player),
]