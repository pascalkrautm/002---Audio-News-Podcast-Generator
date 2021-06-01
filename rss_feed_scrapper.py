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

#User input
#keyword = input("What topic are you interested in? Just type 'keyword' ('corona', 'soccer')")

#rss_feed_scrapper
for url in url_list:
    feed = feedparser.parse(str(url))
    print("Starting scrap " + str(url))
    entries_len = len(feed.entries)
    entry = feed.entries
    print(f"getting {entries_len} entries")
    print("searching for keyword")
    if "corona" in entry:
        feeds.append(feed.entry.title)
        print("adding...")
    else:
        print("no entries found")
