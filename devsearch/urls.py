"""devsearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings #gives access to settings.py file
from django.conf.urls.static import static #for seeing user-uploaded image urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #thisis for setting user-uploaded image urls, not entirely sure what it's doing
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #set url from STATIC_URL to STATIC_ROOT (these are in settings.py)