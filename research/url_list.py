class Url_list():
    """List with news sources to scrap"""
    def __init__(self, url):
        self.url = url

    def url_list(self):
        content = open("url_list.txt", "r")
        content = content.read()
        url_list = content.split(",")
    return url_list()