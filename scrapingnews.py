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


xml_list = []
article_list = []
#url_list
content = open("url_list.txt", "r")
content = content.read()

url_list = content.split(",")
print(url_list)
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

# search for right articles

for xml in xml_list:
    articles = soup.findAll('item')
    for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            content = a.find("description").text
            article = {
                'title': title,
                'link': link,
                "description": content,
                }
            article_list.append(article)
print(article_list)