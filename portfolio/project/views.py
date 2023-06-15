from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.

def index(request):
    projects = Projects.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'project/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    context = {
        'project': project
    }
    return render(request, 'project/detail.html',context)
