from django.urls import path
from . import views

urlpatterns = [
    # path methods take three arguments; 
    # 1. the route which will point towards /'any prepended route in DataScrape urls.py'/ , 
    # 2. the corresponding register method in views.py, and 
    # 3. the alias we are giving the route which can be accessed in our templates with {% url 'alias' %} tags.
    path('', views.index, name='index'),
    path('/examples', views.examples, name='examples'),
]