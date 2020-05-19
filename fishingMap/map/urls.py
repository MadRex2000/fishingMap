from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('fingerling/', views.fingerling, name = 'fingerling'),
    path('areas/', views.areas, name = 'areas'),
    path('month/', views.month, name = 'month'),
    path('tests/', views.tests, name = 'tests'),
]
'''+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)'''
