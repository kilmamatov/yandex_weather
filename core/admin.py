from django.contrib import admin
from core import models


@admin.register(models.Weather)
class Weather(admin.ModelAdmin):
    list_display = ('locality', 'now_dt',)


