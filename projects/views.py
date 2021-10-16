from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]




def projects(request): #request is an HTTP request object
    projects = Project.objects.all() #query to get all Project objects
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk): #pk: dynamic value (primary key)
    projectObj = Project.objects.get(id=pk)
    #tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project':projectObj})
    # if not using template: return HttpResponse('SINGLE PROJECT ' + str(pk))
