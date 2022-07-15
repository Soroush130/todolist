from django.urls import path
from . import views

app_name = 'sport_program'


urlpatterns = [
    path('', views.get_sport_programs, name="get_sport_programs"),
    path('add-program/', views.add_sport_program, name="add_sport_program"),
    path('list-program/', views.list_program_sport, name="list_program_sport"),
    path('delete-program/<int:program_id>/', views.delete_program_sport, name="delete_program_sport"),
    path('detail-program-sport/<int:program_id>/', views.detail_program_sport, name="detail_program_sport"),
    path('new-customize-program/', views.new_customize_program, name="new_customize_program"),
    path('new-customize-item/', views.new_customize_item, name="new_customize_item"),
]
