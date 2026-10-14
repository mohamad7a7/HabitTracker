from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import habit_list_create


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
]
