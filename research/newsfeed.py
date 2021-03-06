import feedparser
import re
#from newsfeed_collection import NewsfeedCollector


class NewsfeedEntry:
    def __init__(self, title: str, summary: str, published: str, link: str):
        self.title = title
        self.summary = summary
        self.clean_summary = clean_summary
        self.published = published
        self.link = link

class Newsfeed:
    def __init__(self, url: str):
        self.feeds = []
        self.url = url
        self.refresh()
        self.entries = []

    def refresh(self):
        self.feed = feedparser.parse(str(self.url))
        self.title = self.feed.channel["title"]
        #entries_len = len(self.feed.entries)
        keyword = input("What topic are you interested in? Just type 'keyword' ('corona', 'soccer')")
        #print(title)
        for entry in self.feed.entries:
            if keyword in entry.title:
                self.clean_summary = re.sub("(<img.*?>)", "", entry.summary, 0, re.IGNORECASE | re.DOTALL | re.MULTILINE)
                self.feeds.append("Neuer Artikel: " + self.feed.feed["title"] + " " + entry.published[3:17] + ", " + entry.title
                             + self.clean_summary)
            else:
                pass

        return self.feeds
