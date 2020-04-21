from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="logApp-home"),
    path('logs/', views.logs, name='logApp-logs'),
]