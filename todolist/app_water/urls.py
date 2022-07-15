from django.urls import path
from . import views

app_name = 'water'

urlpatterns = [
    path('water/', views.water_daily, name='water_daily'),
    path('add_galss_water/', views.add_galss_water, name='add_galss_water'),
    path('delete-glass-water/<int:day_id>/', views.delete_glass_water, name="delete_glass_water"),
    path('edit_glass_water/<int:day_id>/', views.edit_glass_water, name="edit_glass_water"),
]
