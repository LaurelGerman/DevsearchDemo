from django.shortcuts import render
from django.http import HttpResponse

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
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects':projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk): #pk: dynamic value (primary key)
    projectObj = None
    for i in projectsList: #iterate thru project list, if something matches the primary key, return that one as an object
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project':projectObj})
    # if not using template: return HttpResponse('SINGLE PROJECT ' + str(pk))
