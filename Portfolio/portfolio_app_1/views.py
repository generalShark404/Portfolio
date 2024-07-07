from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, "portfolio/index.html", {})

def Projects(request):
    return render(request, "portfolio/projects.html", {})

def ProjectDetail(request, *arg, **kwargs):
    return render(request, "portfolio/project-detail.html", {})