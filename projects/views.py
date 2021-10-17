from django.shortcuts import render, redirect
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

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid(): #django does the validation magically!
                form.save()  #this is what posts it to the database
                return redirect('projects') #back to projects page after form submission
    
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid(): #django does the validation magically!
                form.save()  #this is what posts it to the database
                return redirect('projects') #back to projects page after form submission
    
    context = {'form':form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_object.html')