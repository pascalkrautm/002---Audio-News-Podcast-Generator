class url():
    """List with news sources to scrap"""

    content = open("url_list.txt", "r")
    content = content.read()

    url_list = content.split(",")
    print(url_list)