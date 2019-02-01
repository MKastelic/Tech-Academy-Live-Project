from django.urls import path

from . import views

urlpatterns = [
    path('weather', views.weather_data, name='weather'),
    path('movies', views.movie_data, name='movies'),
    path('nasa', views.nasa_data, name='nasa')
]