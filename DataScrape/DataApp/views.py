from django.shortcuts import render

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import urllib.request
import re

from .models import UserProfile

def weather_data(request):

    # get user zip code from UserProfile 
    # use Selenium to navigate to Weather.gov site
    browser = webdriver.Chrome()
    browser.get('http://weather.gov/')
    browser.find_element_by_name('inputstring').click()
    browser.find_element_by_name('inputstring').send_keys('97124')
    time.sleep(1)
    browser.find_element_by_name('btnSearch').click()
    time.sleep(1)
    url = browser.current_url

    with urllib.request.urlopen(url) as response:
        page = response.read()
    soup = bs(page, 'html.parser')

    # soup.find(id='current_conditions_detail')

    table_tag = soup.table

    # this finds the current temp directly
    temp = soup.find(class_='myforecast-current-lrg').get_text()
    # returns humidity string (i.e. 38%)
    humidity = table_tag.contents[1].get_text()
    line = re.search(r'\d+%', humidity)
    humidity = line.group()
    # returns date and time string from web site of last update
    last_update = table_tag.contents[11].get_text()
    update = re.search(r'\b\d+\s\w+\s\d+:\d+\s\w+\s\w+\b', last_update)
    last_update = update.group()
    context = {
        'temp': temp,
        'humidity': humidity,
        'last_update': last_update
    }

    # parse HTML to extract temp, humidity and update time to localWeather
    return render(request, 'DataApp/weather_data.html', context)
