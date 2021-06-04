from newsfeed_collection import NewsfeedCollector


class PodcastGenerator:
    def __init__(self):
        self.collector = NewsfeedCollector("../url_list.txt")
        self.feeds = self.collector.refresh()

        for feed in self.feeds:
            for entry in feed.entries:
                print(entry.title)




pg = PodcastGenerator()

