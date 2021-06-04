import feedparser
class NewsfeedEntry:
    def __init__(self, title: str, summary: str):
        self.title = title
        self.summary = summary

class Newsfeed:
    def __init__(self, url: str):
        self.url = url
        self.refresh()
        self.entries = []

    def refresh(self):
        feed = feedparser.parse(str(url))
        entries_len = len(feed.entries)
        for entry in feed.entries:
            if keyword in entry.title:
                self.entries.append(NewsfeedEntry(entry.title, entry.summary))
            else:
                pass

        return self.entries
