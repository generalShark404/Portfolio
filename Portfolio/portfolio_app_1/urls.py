from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, Projects, ProjectDetail

urlpatterns = [
    path('', Home, name='home'),
    path('projects', Projects, name='projects'),
    path('project-detail/<int:project_id>', ProjectDetail, name='project-detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)