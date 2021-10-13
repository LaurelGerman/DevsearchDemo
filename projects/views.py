from django.shortcuts import render
from django.http import HttpResponse

def projects(request): #request is an HTTP request object
    return render(request, 'projects/projects.html')

def project(request, pk): #pk: dynamic value
    return render(request, 'projects/single-project.html')
    # if not using template: return HttpResponse('SINGLE PROJECT ' + str(pk))
