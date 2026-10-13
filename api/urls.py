from django.urls import path
from .views import habit_list_create


urlpatterns = [
    path(
        'habits/',
        habit_list_create,
        name='habit-list-create'
    ),
]
