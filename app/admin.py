from django.contrib import admin

from .models import DailyData, DailyUSData


@admin.register(DailyData)
class DailyDataAdmin(admin.ModelAdmin):
    pass


@admin.register(DailyUSData)
class DailyUSDataAdmin(admin.ModelAdmin):
    pass
