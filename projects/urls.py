from django.urls import path
from . import views
urlpatterns = [
    path('',views.projects, name="projects"), #empty string means this is the root domain
    path('project/<str:pk>/',views.project, name="project"), #pk = primary key; can also use slug or int

    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),

    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),

]