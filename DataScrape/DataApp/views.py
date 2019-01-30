from django.shortcuts import get_object_or_404, render

from .models import UserProfile
from .viewmodels import WeatherScraper

def weather_data(request):
    #  Until user login is functional, user zip_code is simply retrieved from the
    #  first record of the database.
    user = get_object_or_404(UserProfile, id=1)
    zipcode = user.zip_code

    weather = WeatherScraper(zipcode)

    # parse HTML to extract temp, humidity and update time to localWeather
    return render(request, 'DataApp/weather_data.html', {'weather': weather})
