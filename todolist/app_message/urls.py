from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('message-list/', views.message_list, name='message_list'),
    path('send-message/', views.send_message, name='send_message'),
    path('delete-message/<int:message_id>/', views.delete_messsage, name='delete_messsage'),
]
