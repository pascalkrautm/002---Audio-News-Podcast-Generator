class Rss_feed_scrapper():
    def __init__(self):
        url_list.self = url_list()


    def url_list(self):
        content = open("url_list.txt", "r")
        content = content.read()
        url_list = content.split(",")
    return url_list()

    def user_input(self):
        keyword = input("What topic are you interested in? Just type 'keyword' ('corona', 'soccer')")

    def ssl_check(self):
        ssl._create_default_https_context = ssl._create_unverified_context

    def feed_scrapper(self):
        for url in url_list:
            feed = feedparser.parse(str(url))
            print("Starting scrap " + str(url))
            entries_len = len(feed.entries)
            print(f"getting {entries_len} entries")
            print("searching for keyword")
            for entry in feed.entries:
                if keyword in entry.title:
                    # testline
                    print(entry.title)
                    # testline
                    print(entry.summary)
                    feeds.append(entry.summary)
                else:
                    pass
    return(feeds)

    del feed_deleter(self):
    feeds[:]




