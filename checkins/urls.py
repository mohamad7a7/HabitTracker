from django.urls import path
from .import views


urlpatterns = [
    path(
        'toggle/<int:habit_id>/',
        views.toggle_checkin,
        name='toggle_checkin'
    ),
]
