import feedparser
import re
from tqdm import tqdm
from multiprocessing import Pool
import time


class PodcastGenerator:
    def __init__(self):

        self.xml_list = []
        self.article_list = []
        self.feeds = []
        file = open("url_list.txt", "r")
        self.content = file.read()
        self.url_list = self.content.split(",")

    def generate_podcast(self, keywords):
        """
        Generate podcost from current url list.
        :param keyword: The keyword to filter content for
        :return:
        """
        self.number_of_posts = 0
        # self.keyword = keyword
        self.keywords = keywords
        self.get_feed_data()
        self.text = self.clean_data()

        return self.number_of_posts > 0

    def get_feed_data(self):
        counter = 0
        ticks = len(self.url_list)
        with tqdm(total=ticks, leave=False) as progress_bar:
            progress_bar.set_description("Scraping")
            counter = 0

            # rss_feed_scrapper
            for url in self.url_list:
                feed = feedparser.parse(str(url))

                entries_len = len(feed.entries)
                # print(f"getting {entries_len} entries")
                # print("searching for keyword")


                for entry in feed.entries:
                    for keyword in self.keywords:
                        if keyword in entry.title.lower():
                            clean_summary = re.sub("(<img.*?>)", "", entry.summary, 0, re.IGNORECASE | re.DOTALL |
                                                   re.MULTILINE)
                            self.feeds.append(
                                "Neuer Artikel: " + feed.feed["title"] + " " + entry.published[3:17] + ", " + entry.title
                                + clean_summary)
                            self.number_of_posts += 1

                for i in range(len(self.feeds)):
                    self.feeds[i] = self.feeds[i].lower()

                counter += 1
                progress_bar.update(counter)
            progress_bar.update(ticks)

            # progress_bar.close()
            # tqdm(ticks, ncols=ticks)
            # for i in tqdm(range(0, 100), ncols=100):
            #     time.sleep(.01)

    def clean_data(self, save_to_disc: bool = False):
        """
        Cleans feed data for reading.
        :param save_to_disc: (optional) Set to True to save file to disk, otherwise False.
        :return: the cleaned text, ready for reading
        """
        feeds_clean = str(self.feeds)
        feeds_clean = feeds_clean.replace("</p>'", " ").replace("<p>", ".")
        # print(feeds_clean)

        if save_to_disc:
            file = open(r'podcast.txt', 'w', encoding='utf-8')
            file.write(feeds_clean)
            file.close()

        return feeds_clean

    def read_podcast(self):
        pass
