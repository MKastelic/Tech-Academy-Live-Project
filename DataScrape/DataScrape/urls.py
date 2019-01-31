"""DataScrape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from DataApp import views

urlpatterns = [
    path('', include('HomeApp.urls')), # the include method accepts an argument of an iterable (the urlpatterns list in each App's urls.py folder)
    path('admin/', admin.site.urls),
    path('data/', include('DataApp.urls')),
    # Django allows us to use the same 'accounts/' route name when working with urls; this route name is arbitrary though so we can define it however we want.
    path('accounts/', include('AccountsApp.urls')),
    path('users/', include('django.contrib.auth.urls')) # the django.contrib.auth included in settings.py provides us with pre-existing Views and URLs; Django will look for templates in a registration folder we create within the templates folder.
]
