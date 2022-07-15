from django.contrib import admin
from .models import WaterDaily

class WaterDailyAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'count']

admin.site.register(WaterDaily, WaterDailyAdmin)