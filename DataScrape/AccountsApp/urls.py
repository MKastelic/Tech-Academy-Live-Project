from django.urls import path
from . import views


urlpatterns = [
    # path methods take three arguments; 
    # 1. the route which will point towards /'any prepended route in DataScrape urls.py'/register, 
    # 2. the corresponding register method in this App's views.py file, and 
    # 3. the alias we are giving the route which can be accessed in our templates with {% url 'alias' %} tags.
    path('register', views.register, name='register'),
]