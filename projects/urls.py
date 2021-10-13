from django.urls import path
from . import views
urlpatterns = [
    path('',views.projects, name="projects"), #empty string means this is the root domain
    path('project/<str:pk>/',views.project, name="project"), #pk = primary key; can also use slug or int
]