from django.urls import path

from . import views

urlpatterns = [
    path('weather', views.weather_data, name='weather'),
    path('movies', views.movie_data, name='movies'),
    path('events', views.events_data, name='events'),
    path('nasa', views.nasa_data, name='nasa'),
    path('tech_event', views.tech_events_data, name='tech_event'),
    path('stitcher', views.stitcher_data, name='stitcher'),
]