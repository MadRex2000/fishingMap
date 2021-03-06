from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

#url path that can path to html by urls

urlpatterns = [
    path('', views.home, name = 'home'),
    path('fingerling/', views.fish, name = 'fingerling'),
    path('areas/', views.areas, name = 'areas'),
    path('tests/', views.tests, name = 'tests'),
    path('report/', views.fishingStatusReport, name = 'report')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
