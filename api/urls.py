from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import habit_list_create, habit_detail, checkin_list_create, register


urlpatterns = [
    path(
        'auth/token/',
        obtain_auth_token,
        name='api-token-auth'
    ),
    path(
        'habits/',
        habit_list_create,
        name='habit-list-create'
    ),
    path(
        'habits/<int:pk>/',
        habit_detail,
        name='habit-detail'
    ),
    path(
        'checkins/',
        checkin_list_create,
        name='checkin-list-create'
    ),
    path('auth/register/',
         register,
         name='api-register'),
]
