from podcast import Podcast

from mp3converter import Converter
from newsfeed_collection import NewsfeedCollector


class PodcastGenerator:
    def __init__(self):
        self.collector = NewsfeedCollector("../url_list.txt")
        self.feeds = self.collector.refresh()
        self.formatter = Podcast()
        self.cleaner = self.formatter.clean()
        self.converter = Converter()

        self.xml_list = []
        self.article_list = []
        self.feeds = []
        self._content =

        # url_list
        content = open("url_list.txt", "r")
        content = content.read()
        url_list = content.split(",")
        print(url_list)

    def generate_podcast(self, keyword: str):

        pass

    def read_podcast(self):
        pass







if __name__ == "__main__":
    pg = PodcastGenerator()

