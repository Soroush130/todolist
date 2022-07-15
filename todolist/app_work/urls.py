from django.urls import path
from . import views
app_name = 'work'

urlpatterns = [
    path('add-work/', views.add_work, name='add_work'),
    path('check_work/', views.check_work, name='check_work'),
    path('delete-work/<int:work_id>/', views.delete_work, name='delete_work'),
    ###############
    #   System Tag
    ###############
    path('tags/', views.tags, name='tags'),
    path('add-tag/', views.add_tag, name='add_tag'),
    path('report-tag/', views.reporting_tag, name='reporting_tag'),
    ###############
    #    Scoring system
    ###############
    path('scoring/', views.scoring, name="scoring"),
    path('score-points/', views.score_points, name="score_points"),
    path('score-detail/<int:score_id>/', views.score_detail, name="score_detail"),
    path('score-edit/<int:score_id>/', views.score_edit, name="score_edit"),
    path('score-delete/<int:score_id>/', views.score_delete, name="score_delete"),
    #################
    path('show-percent-work-daily-bar/', views.show_percent_work_daily_to_bar, name='show_percent_work_daily_to_bar'),
    path('show-percent-work-daily-circle/', views.show_percent_work_daily_to_circle, name='show_percent_work_daily_to_circle'),
    path('calc-percent-work-daily/', views.calc_percent_work_daily, name='calc_percent_work_daily'),
    path('calc-percent-to-circle/', views.calc_percent_to_circle, name="calc_percent_to_circle")
]