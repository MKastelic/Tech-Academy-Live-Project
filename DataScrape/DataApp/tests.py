from django.test import TestCase
from bs4 import BeautifulSoup as bs
from selenium import webdriver

# Create your tests here.
class TechUpcomingScraper:

    def __init__(self):

        # Use Selenium to navigate to bizzabo's site using chrome driver at the specified path.
        browser = webdriver.Chrome('DataApp/bin/chromedriver.exe')
        browser.get('https://blog.bizzabo.com/technology-events')

        #time.sleep(1)

        # the new page with events generated for the user's city and state will be stored using Selenium's page_source function
            # we need to use .page_source because urllib's request method only returns html and not JavaScript related code? (I read this somewhere along the way, will have to go back and clarify).
        # then, the information will be parsed with Beautiful Soup, at which point we can grab all of the divs that hold relevant event data.
        html = browser.page_source
        soup = bs(html, 'html.parser')
        # find_all returns a Beautiful Soup ResultSet (list)
        target = soup.find_all('div', class_='event-feed-item')
        print(html)
        print(soup)