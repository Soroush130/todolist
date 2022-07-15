from django.urls import path
from . import views

app_name = 'reminder'

urlpatterns = [
    path('reminders/', views.reminders, name="reminders"),
    path('add-reminder/', views.add_reminder, name="add_reminder"),
]
