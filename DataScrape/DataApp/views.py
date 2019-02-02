from django.shortcuts import get_object_or_404, render

from .models import UserProfile
from django.contrib.auth.models import User
from .viewmodels import WeatherScraper, MovieScraper, EventScraper


def weather_data(request):
    #  Until user login is functional, user zip_code is simply retrieved from the
    #  first record of the database.
    user = get_object_or_404(UserProfile, id=1)
    zipcode = user.zip_code

    #  WeatherScraper object is initialized with temperature, humidity, and last update
    #  time from the Weather.gov site page result obtained using the passed zipcode
    #  parameter to search for the local weather forecast.
    weather = WeatherScraper(zipcode)

    return render(request, 'DataApp/weather_data.html', {'weather': weather})


def movie_data(request):

    # MovieScraper object has a movie_list attribute which contains the list of the
    # current top 5 box office movies from Imdb.
    movie = MovieScraper()
    return render(request, 'DataApp/movie_data.html', {'movie': movie})


def events_data(request):

    user = request.user
    current_profile = get_object_or_404(UserProfile, user_id=user.id)
    city = current_profile.city
    state = current_profile.state

    event = EventScraper(city, state)

    context = {
        'event': event,
    }

    return render(request, 'DataApp/events_data.html', context)