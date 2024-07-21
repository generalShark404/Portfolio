from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, ProjectFeature, ProjectImages,Person


# Create your views here.
def Home(request):
    person = Person.objects.get(id=1)
    return render(request, "portfolio/index.html", {'me':person})

def Projects(request):
    projects = Project.objects.all()
    return render(request, "portfolio/projects.html", {'projects':projects})

def ProjectDetail(request, *arg, **kwargs):
    id = kwargs.get('project_id', None)
    project = Project.objects.get(id=id)
    project_feature = ProjectFeature.objects.filter(project=id)
    project_images = ProjectImages.objects.filter(project=id)
    print(project_images)
    return render(request, "portfolio/project-detail.html", {'project':project,'features':project_feature,'images':project_images})