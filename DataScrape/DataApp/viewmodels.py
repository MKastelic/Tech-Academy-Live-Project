import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import urllib.request
import json
import re


class WeatherScraper:

    def __init__ (self, zip):
        self.zipcode = zip

    #  Use Selenium to navigate to Weather.gov site.  The specific browser driver location
    #  required for instantiation is provided as a path in the call to Chrome().

        browser = webdriver.Chrome('DataApp/bin/chromedriver.exe')
        browser.get('http://weather.gov/')

        #  Upon landing at Weather.gov, the "Local forecast by" search box must be clicked to
        #  remove default "Enter location" text before sending the user's zipcode.
        browser.find_element_by_name('inputstring').click()
        browser.find_element_by_name('inputstring').send_keys(self.zipcode)

        #  Wait a while until the "Local forecast" search returns with alternate results for the
        #  user's zipcode before clicking the "Go" button to actually begin the search for local data.
        time.sleep(1)
        browser.find_element_by_name('btnSearch').click()

        #  Again wait a while until the page refreshes from the local data search before getting the
        #  URL info from the results page.
        time.sleep(1)
        url = browser.current_url

        #  Open the URL above for local forecast and get the HTML to parse with Beautiful Soup 4 (BS4)
        with urllib.request.urlopen(url) as response:
            page = response.read()
        soup = bs(page, 'html.parser')

        #  Close the browser opened for Weather.gov. 
        #  ToDo:  Can the whole operation of opening the browser be made silent, so the user doesn't see it?
        browser.quit()

        # BS4 allows easy extraction of local temperature data by looking at a unique class identifier.
        self.temp = soup.find(class_='myforecast-current-lrg').get_text()

        #  For the humidity and last update info a slightly more sophisticated drill down is required.
        #  Without a unique class or id we need to look for specific text within <b> tags.
        #  Begin search by looping through each item contained in the only table on the results page.
        for index,item in enumerate(soup.table.contents):
            #  Try block allows passing of exception thrown when items do not contain <b> tags.
            #  "AttributeError: 'NavigableString' object has no attribute 'b'.
            try:
                if soup.table.contents[index].b.get_text() == 'Humidity':
                    humidity = soup.table.contents[index].get_text()
                    #  Text returned for item contains the <b> tag string, so regex extracts just the humidity
                    #  or last_update values.
                    humidity = re.search(r'\d+%', humidity)
                    #  re.search returns an object and the "matched" string is retrieved with the group() method.
                    self.humidity = humidity.group()
                if soup.table.contents[index].b.get_text() == 'Last update':
                    last_update = soup.table.contents[index].get_text()
                    last_update = re.search(r'\b\d+\s\w+\s\d+:\d+\s\w+\s\w+\b', last_update)
                    self.last_update = last_update.group()
            except:
                pass


class MovieScraper:

    def __init__ (self):

        #  Open the URL for the Imdb top box office page and get the HTML to parse with Beautiful Soup 4 (BS4)
        with urllib.request.urlopen('https://www.imdb.com/chart/boxoffice') as response:
            page = response.read()
        soup = bs(page, 'html.parser')
        
        #  In typical French culinary tradition, perform a soup reduction to narrow the parsed HTML results
        #  to only the anchor tags within a single table element.
        movies = soup.table.find_all('a')
        pattern = re.compile(r'\w+')
        self.movie_list = []
        
        #  Not all anchor tags in the top box office table have text (only those that link to the movie name).
        #  Loop through the first ten anchors and add only those with movie name text to the movie_list attribute.
        for index in range(0,10):
            if re.search(pattern, movies[index].get_text()):
                self.movie_list.append(movies[index].get_text())


class NasaScraper:

    def __init__ (self):

        #  Open the URL for the NASA API endpoint for their Astronomy Picture of the Day (APOD) and provide required
        #  API key to allow limited rate access to this resource.
        url = 'https://api.nasa.gov/planetary/apod?api_key=kK4OwaUtVghqi9A1m40BsWAueYlagAIUQFM6FYlw'
        serialized_data = urllib.request.urlopen(url).read()

        #  Load JSON response into data object and access known key names in order to set NasaScraper attributes.
        data = json.loads(serialized_data)
        self.image_src = data['url']
        self.title = data['title']
        self.detail = data['explanation']
        self.date = data['date']
            