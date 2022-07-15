from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.notes, name='notes'),
    path('add-note/', views.add_note, name='add_note'),
    path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
]