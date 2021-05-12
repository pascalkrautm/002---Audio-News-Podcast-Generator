import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

class SiteCheck():
    """Looking for news on given website. Checking site status"""
    def url_opener(self):
        pass

    def get_xml(self):
        pass

class get_articles():
    """parsing for description in news"""
class SourceList():
    """List with news sources to scrap"""

# Source List
url_list = ["https://rss.sueddeutsche.de/rss/Topthemen","https://www.haz.de/rss/feed/haz_schlagzeilen"]
xml_list = []

# scraping function

for url in url_list:
    print("Starting scrap " + str(url))
    try:
        r = requests.get(url)
        print("Scraping succeeded. See: ", r.status_code)
        try:
            soup = bs(r.content, "lxml")
            xml_list.append(soup)
            print("creating xml succeeded")
        except:
            print("Error while creating xml")
    except Exception as e:
        print("The scraping job failed. See: ")
        print(e)
print(xml_list)
