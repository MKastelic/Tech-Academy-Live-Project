from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
import urllib.request
import json

from .models import UserProfile
from django.contrib.auth.models import User
from .viewmodels import WeatherScraper, MovieScraper, EventScraper, NasaScraper, TechUpcomingScraper, PodcastScraper, NHLScraper




def weather_data(request):

    # retrieve the current logged in user.
    user = request.user
    # get the user's data from the UserProfile model using the OneToOne user_id field.
    current_profile = get_object_or_404(UserProfile, user_id=user.id)
    # store the user's zipode in a variable
    zipcode = current_profile.zip_code

    #  WeatherScraper object is initialized with temperature, humidity, and last update
    #  time from the Weather.gov site page result obtained using the passed zipcode
    #  as a parameter to search for the local weather forecast.
    weather = WeatherScraper(zipcode)

    return render(request, 'DataApp/weather_data.html', {'weather': weather})


def movie_data(request):

    # MovieScraper object has a movie_list attribute which contains the list of the
    # current top 5 box office movies from Imdb.
    movie = MovieScraper()
    return render(request, 'DataApp/movie_data.html', {'movie': movie})


def events_data(request):

    # retrieve the current logged in user.
    user = request.user
    # get the user's data from the UserProfile model using the OneToOne user_id field.
    current_profile = get_object_or_404(UserProfile, user_id=user.id)
    # store the user's city and state in variables.
    city = current_profile.city 
    state = current_profile.state

    # create an instance of the EventScraper class
    event = EventScraper(city, state)

    context = {
        'event': event,
    }

    # pass the context object into the render method so that we'll have access to the relevant data.
    return render(request, 'DataApp/events_data.html', context)
def nasa_data(request):
    
    # NasaScraper object has attributes for date, source url, title, and description for
    # the NASA Astronomy image of the day.
    nasa = NasaScraper()
    return render(request, 'DataApp/nasa_data.html', {'nasa': nasa})


def tech_events_data(request):

    tech_event = TechUpcomingScraper()
    return render(request, 'DataApp/tech_upcoming_data.html', {'tech_event': tech_event})
def stitcher_data(request):

    podcast = PodcastScraper()

    context = {
        'podcast': podcast,
    }

    return render(request, 'DataApp/stitcher_data.html', context)

def nhl_data(request):

    #  retrieve the current logged in user.
    user = request.user
    #  get the user's data from the UserProfile model using the OneToOne user_id field.
    current_profile = get_object_or_404(UserProfile, user_id=user.id)
    #  store the user's favorite NHL team in a variable 
    favorite_nhl_team = current_profile.favorite_nhl_team
    #  create an instance of the NHLScraper class, passing the user's favorite team name.
    nhl = NHLScraper(favorite_nhl_team)
    #  pass the context object nhl into the render method to supply needed data.
    return render(request, 'DataApp/nhl_data.html', {'nhl': nhl})
