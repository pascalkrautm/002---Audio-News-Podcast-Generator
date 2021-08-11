import re
import ssl
import feedparser
from tqdm import tqdm


class PodcastGenerator:
    def __init__(self):
        """The PodcastGenerator class is initialized"""
        self.xml_list = []
        self.article_list = []
        self.feeds = []
        file = open("url_list.txt", "r")
        self.content = file.read()
        self.url_list = self.content.split(",")
        self.number_of_posts = []
        self.keywords = ()
        self.text = self.clean_data()

    def generate_podcast(self, keywords):
        """
        Generate podcast from current url list.
        :return: Number of articles that include the keywords.
        """
        self.number_of_posts = 0
        self.keywords = keywords
        self.get_feed_data()
        self.text = self.clean_data()

        return self.number_of_posts > 0

    def get_feed_data(self):
        """
        Create a List with all articles that include the keywords.
        :return: List with all article that include the keywords
        """
        ssl._create_default_https_context = ssl._create_unverified_context
        ticks = len(self.url_list)
        with tqdm(total=ticks, leave=False) as progress_bar:
            progress_bar.set_description("Scraping")
            counter = 0

            for url in self.url_list:
                feed = feedparser.parse(str(url))
                for entry in feed.entries:
                    for keyword in self.keywords:
                        if str(keyword) in entry.title.lower():
                            clean_summary = re.sub("(<.*?>)", "", entry.summary, 0, re.IGNORECASE | re.DOTALL |
                                                   re.MULTILINE)
                            try:
                                pubdate = entry.published
                            except:
                                pubdate = ""

                            self.feeds.append(
                                "New Article: " + feed.feed["title"] + " " + pubdate[3:17] + ", "
                                + entry.title + ". " + clean_summary)
                            self.number_of_posts += 1

                for i in range(len(self.feeds)):
                    self.feeds[i] = self.feeds[i].lower()

                counter += 0.5
                progress_bar.update(counter)
            progress_bar.update(ticks)
            print("Scraping done! Process finished: 100%")

    def clean_data(self):
        """
        Cleans feed data for reading.
        :return: the cleaned text, ready for reading
        """
        feeds_clean = str(self.feeds)
        feeds_clean = feeds_clean.replace("</p>'", " ").replace("<p>", ".").replace("<h1>", " ").replace("</h1>", " ") \
            .replace("</p>", " ").replace("<hr />.", " ")
        return feeds_clean
