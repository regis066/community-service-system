from django.urls import path
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('', views.list_volunteers, name='list_volunteers'),
    path('new/', views.create_volunteer, name='create_volunteer'),
]
