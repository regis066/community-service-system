from django.urls import path
from . import views

app_name = 'service_hours'

urlpatterns = [
    path('', views.list_service_hours, name='list_service_hours'),
    path('new/', views.create_service_hour, name='create_service_hour')
]
