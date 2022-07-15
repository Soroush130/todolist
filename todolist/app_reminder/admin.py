from django.contrib import admin
from .models import Reminder, MotivationalPhrases


class ReminderAdmin(admin.ModelAdmin):
    list_display = ['title', '__str__']
admin.site.register(Reminder, ReminderAdmin)


admin.site.register(MotivationalPhrases)