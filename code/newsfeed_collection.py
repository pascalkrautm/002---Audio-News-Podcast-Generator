import feedparser
from newsfeed import Newsfeed
from formatter_new import feeds


class NewsfeedCollector:
    def __init__(self,path:str):
        self.path = path
        self.feeds = []

    def refresh(self):
        self.feeds.clear()
        content = open(self.path, "r")
        content = content.read()
        url_list = content.split(",")
        print(url_list)

        for url in url_list:
            self.feeds.append(Newsfeed(url))

        return self.feeds


