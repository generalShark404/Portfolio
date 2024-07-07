from django.urls import path
from .views import Home, Projects, ProjectDetail

urlpatterns = [
    path('', Home, name='home'),
    path('projects', Projects, name='projects'),
    path('project-detail/<int:project_id>', ProjectDetail, name='project-detail')
]