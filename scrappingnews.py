class SiteCheck():
    """Looking for news on given website. Checking site status"""
class Downloader():
    """Downloading news  in txt"""
class SourceList():
    """List with news sources to scrap"""

# Source List
#url_list = ["https://rss.sueddeutsche.de/rss/Topthemen"]

#scraping function
# scraping function

def url_opener(url):
    print("Starting scraping" + {url})
    try:
        r = requests.get()
        return print("Finished scraping" + str{url} + "with: ", r.status_code)
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)


import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://rss.sueddeutsche.de/rss/Topthemen"

url_opener(url)


pagesToGet = 1

upperframe = []
for page in range(1, pagesToGet + 1):
    print('processing page :', page)
    #make a list of sites from range pages to Get
    url = 'https://www.politifact.com/factchecks/list/?page=' + str(page)
    print(url)

    # an exception might be thrown, so the code should be in a try-except block
    try:
        # use the browser to get the url. This is suspicious command that might blow up.
        page = requests.get(url)  # this might throw an exception if something goes wrong.

    except Exception as e:  # this describes what to do if an exception is thrown
        error_type, error_obj, error_info = sys.exc_info()  # get the exception information
        print('ERROR FOR LINK:', url)  # print the link that cause the problem
        print(error_type, 'Line:', error_info.tb_lineno)  # print error info and line that threw the exception
        continue  # ignore this page. Abandon this and go back.
    time.sleep(2)
    page.status_code
    page.text
    soup = BeautifulSoup(page.text, 'html.parser')
    frame = []
    links = soup.find_all('li', attrs={'class': 'o-listicle__item'})
    print(len(links))
    filename = "NEWS.csv"
    f = open(filename, "w", encoding='utf-8')
    headers = "Statement,Link,Date, Source, Label\n"
    f.write(headers)

    for j in links:
        Statement = j.find("div", attrs={'class': 'm-statement__quote'}).text.strip()
        Link = "https://www.politifact.com"
        Link += j.find("div", attrs={'class': 'm-statement__quote'}).find('a')['href'].strip()
        Date = j.find('div', attrs={'class': 'm-statement__body'}).find('footer').text[-14:-1].strip()
        Source = j.find('div', attrs={'class': 'm-statement__meta'}).find('a').text.strip()
        Label = j.find('div', attrs={'class': 'm-statement__content'}).find('img',
                                                                            attrs={'class': 'c-image__original'}).get(
            'alt').strip()
        frame.append((Statement, Link, Date, Source, Label))
        f.write(Statement.replace(",", "^") + "," + Link + "," + Date.replace(",", "^") + "," + Source.replace(",",
                                                                                                               "^") + "," + Label.replace(
            ",", "^") + "\n")
    upperframe.extend(frame)
f.close()
data = pd.DataFrame(upperframe, columns=['Statement', 'Link', 'Date', 'Source', 'Label'])
data.head()
