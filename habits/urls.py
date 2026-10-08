from django.urls import path
from . import views


urlpatterns = [
    path(
        'create/',
        views.create_habit,
        name='create_habit'
    ),

    path(
        'delete/<int:habit_id>/',
        views.delete_habit,
        name='delete_habit'
    ),

    path(
        'edit/<int:habit_id>/',
        views.edit_habit,
        name='edit_habit'
    ),
]
