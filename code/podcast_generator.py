from podcast import Podcast

from mp3converter import Converter
from newsfeed_collection import NewsfeedCollector


class PodcastGenerator:
    def __init__(self):
        self.collector = NewsfeedCollector("../url_list.txt")
        self.feeds = self.collector.refresh()
        self.formatter = Podcast()
        self.cleaner = self.formatter.clean()
        self.saver = self.formatter.save()
        self.converter = Converter()

        for feed in self.feeds:
            for entry in feed.entries:
                print(entry)



if __name__ == "__main__":
    pg = PodcastGenerator()

