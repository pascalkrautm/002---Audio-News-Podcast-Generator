import feedparser

from formatter_new import keyword


class NewsfeedEntry:
    def __init__(self, title: str, summary: str, published: str, link: str):
        self.title = title
        self.summary = summary
        self.clean_summary = clean_summary
        self.published = published
        self.link = link

class Newsfeed:
    def __init__(self, url: str):
        self.url = url
        self.refresh()
        self.entries = []

    def refresh(self):
        feed = feedparser.parse(str(self.url))
        self.title = feed.channel["title"]
        entries_len = len(feed.entries)
        keyword = input("What topic are you interested in? Just type 'keyword' ('corona', 'soccer')")
        #print(title)
        for entry in feed.entries:
            if keyword in entry.title:
                self.clean_summary = re.sub("(<img.*?>)", "", entry.summary, 0, re.IGNORECASE | re.DOTALL | re.MULTILINE)
                #self.entries.append(NewsfeedEntry(entry.title, entry.abstract, entry.published, entry.link))
                self.feeds.append(NewsfeedEntry(feed.feed["title"], entry.published, entry.title, clean_summary))
            else:
                pass

        return self.feeds
