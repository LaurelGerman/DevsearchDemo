from django.http import JsonResponse

def getRoutes(request): #this is basically api documentation

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},  
    ]

    return JsonResponse(routes, safe=False) #go ahead and turn any data we want into json, not just a single dictionary