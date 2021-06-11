import feedparser

from formatter_new import keyword


class NewsfeedEntry:
    def __init__(self, title: str, summary: str, published: str, link: str):
        self.title = title
        self.summary = summary
        self.published = published
        self.link = link

class Newsfeed:
    def __init__(self, url: str):
        self.url = url
        self.refresh()
        self.entries = []

    def refresh(self):
        feed = feedparser.parse(str(self.url))
        title = feed["title"]
        entries_len = len(feed.entries)
        keyword = input("What topic are you interested in? Just type 'keyword' ('corona', 'soccer')")
        for entry in feed.entries:
            if keyword in entry.title:
                self.entries.append(NewsfeedEntry(entry.title, entry.summary, entry.published, entry.link))
            else:
                pass

        return self.entries
