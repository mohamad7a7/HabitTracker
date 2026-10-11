from django.contrib import admin
from .models import CheckIn


class CheckInAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date', 'is_done', 'created_at')


admin.site.register(CheckIn, CheckInAdmin)
