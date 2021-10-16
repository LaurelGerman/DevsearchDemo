from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm





def projects(request): #request is an HTTP request object
    projects = Project.objects.all() #query to get all Project objects
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk): #pk: dynamic value (primary key)
    projectObj = Project.objects.get(id=pk)
    #tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project':projectObj})
    # if not using template: return HttpResponse('SINGLE PROJECT ' + str(pk))


def createProject(request):
    form = ProjectForm()
    context = {'form':form}
    return render(request, "projects/project_form.html", context)