from django.urls import path

from . import views

urlpatterns = [
    path('weather', views.weather_data, name='weather'),
    path('movies', views.movie_data, name='movies'),
    path('events', views.events_data, name='events'),
    path('nasa', views.nasa_data, name='nasa'),
    path('stitcher', views.stitcher_data, name='stitcher'),
    path('nhl', views.nhl_data, name='nhl')
]