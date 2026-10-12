from django.urls import path, include
from . import views


urlpatterns = [
    path(
        'create/',
        views.create_habit,
        name='create_habit'
    ),
    path('<int:habit_id>/', include(
        [
            path(
                'delete',
                views.delete_habit,
                name='delete_habit'
            ),

            path(
                'edit',
                views.edit_habit,
                name='edit_habit'
            ),

            path(
                'toggle-status',
                views.toggle_habit_status,
                name='toggle_habit_status'
            ),
        ]))
]
