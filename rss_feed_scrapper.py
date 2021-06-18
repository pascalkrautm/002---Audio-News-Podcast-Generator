import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import feedparser
import ssl
import re

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
    #print(feed.entries)
    for entry in feed.entries:
        if keyword in entry.title:
            #testline
            #print(entry.title)
            #testline
            #print(entry.summary)
            #print(entry.published)
            clean_summary = re.sub("(<img.*?>)", "", entry.summary, 0, re.IGNORECASE | re.DOTALL | re.MULTILINE)
            feeds.append(feed.feed["title"] + " " + entry.published + entry.title + clean_summary)
        else:
            pass

print(feeds)

feeds_clean = str(feeds)
feeds_clean_new = feeds_clean.replace("</p>'", "")
feeds_clean_new1 = feeds_clean_new.replace("<p>", ".")
print(feeds_clean_new1)


