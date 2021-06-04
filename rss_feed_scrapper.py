import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import feedparser
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

xml_list = []
article_list = []
feeds = []

#url_list
content = open("url_list.txt", "r")
content = content.read()
url_list = content.split(",")
print(url_list)
#User input
keyword = input("What topic are you interested in? Just type 'keyword' ('corona', 'soccer')")

#liste leeren
del feeds[:]

#rss_feed_scrapper
for url in url_list:
    feed = feedparser.parse(str(url))
    print("Starting scrap " + str(url))
    entries_len = len(feed.entries)
    print(f"getting {entries_len} entries")
    print("searching for keyword")
    for entry in feed.entries:
        if keyword in entry.title:
            #testline
            print(entry.title)
            #testline
            print(entry.summary)
            feeds.append(entry.summary & entry.title)
        else:
            pass

print(feeds)

import re
feeds_new = str(feeds)

feeds_clean = str(re.findall("<p>(.*?)</p>", feeds_new, re.DOTALL))
print(feeds_clean)

myText = open(r'test1.txt','w')
myString = feeds_clean
myText.write(myString)
myText.close()

