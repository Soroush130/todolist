from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from app_work import views as view_work

urlpatterns = [
    path('admin/', admin.site.urls),
    path('header', views.header, name="header"),
    path('footer', views.footer, name="footer"),
    path('404/', views.page_404, name="page_404"),
    ######################
    path('', view_work.profile, name='home'),
    path('work/', include("app_work.urls")),
    ######################
    path('note/', include("app_note.urls")),
    ######################
    path('accounts/', include("app_account.urls")),
    ######################
    path('message/', include("app_message.urls")),
    ######################
    path('water/', include("app_water.urls")),
    ######################
    path('reminder/', include("app_reminder.urls")),
    ######################
    path('sport/', include("app_sports_program.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
