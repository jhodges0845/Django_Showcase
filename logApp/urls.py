from django.urls import path
from .views import (LogListView, LogDetailView,
                     LogCreateView, LogUpdateView, LogDeleteView)
from . import views

urlpatterns = [
    path('', views.home, name="logApp-home"),
    path('logs/<int:pk>/', LogDetailView.as_view(), name="logApp-detail"),
    path('logs/update/<int:pk>/', LogUpdateView.as_view(), name="logApp-update"),
    path('logs/delete/<int:pk>/', LogDeleteView.as_view(), name="logApp-delete"),
    path('logs/new/', LogCreateView.as_view(), name="logApp-create"),
    path('logs/', LogListView.as_view(), name='logApp-logs'),
]