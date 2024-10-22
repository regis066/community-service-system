from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.list_projects, name='list_projects'),
    path('new/', views.create_project, name='create_project'),
]