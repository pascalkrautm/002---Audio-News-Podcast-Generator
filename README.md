- Pascal Krautmacher [697450]
- Eren Ünal [859039]
- Marco Alexander Meinhold [872406]

# 002---Audio-News-Podcast-Generator
002 - Audio News Podcast Generator, MBA HSD SS21

The file README.md represents the central entry point and your main contributions for the evaluation and examination of the given use case. This document needs to contain at least 10.000 characters, but not more than 100.000 characters.

Important: The number of characters in will be evaluated by automated processes and, if outside this range, will reduce the grading of the use case evaluation by 0,5 grades (from 1.0 best down to 6.0 worst). Hence, better count your characters...

For advice on how to write and format MarkDown files please visit (either or both):

https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
The README.md file must be written in English language (expections on request only) and has to contain the following mandatory information in the following order:

At the very top of the file, a list of first name and last name followed by the matriculation number in squared brackets '[...]' for all students involved in and to be evaluated for the given use case. Other contributors must be listed without brackets and marticulation number. Sample: The following markdown code would create a valid output. Only Peter Parker and Precilla Presley will evaluted for the use case.

- Peter Peter [7436450]
- Precilla Presley [7442803]
- Bob the Bausmeister (supporting on GitHub Actions)
- Sharon Zurkoswsky
The title of the use case, exactly as defined by the lecturer (letter by letter) formatted as top level headline.Sample for valid markdown:

### Business Analytics A - Use Case 
**[...back to use case list](/../../blob/main/README.md)**

# 002 - Audio News Podcast Generator
**Summary**: Automated generation of a podcast from relevant news
available on the internet.
### 1. Use Case Classification
**Complexity:**  low to medium complex use case with focus on the selection and 
orchestration of various Python packages to get the job done. 

**Challenges:** NewsFeed processing, (optional)Web Scraping, Text-to-Speech, 
Commandline parsing, progress/status visualization in commandline,
execution on Windows and Mac.

**Team setup:** 2 to 3 students.

### 2. Story
>Fight the Corona blues! 

**Me:** *I'm so bored, please read out something interesting to me.*

**You:** *No problem, I'm a Python hero!*

### 3. Functional Requirements / Expected Results
Create a command line tool, named **podgen.py** that... 

1. ...comes with a configuration file containing a user-editable list of news 
   sources to be investigated. The primary news source should be public 
   RSS or AtomFeeds, but additional sources are also welcome.
   
   The configuration file should contain a list of at least 30 RSS feeds
   from popular news sources like CNN, NYT, FoxNews, Spiegel an others. 


2. ...takes a list of comma separated keywords or phrases arguments to used 
   to generate and filter the podcast. Some valid samples:
   - **podgen.py Corona**
   - **podgen.py "Angela Merkel"** 
   - **podgen.py "Donald Trump" "Joe Biden"** 
   - **podgen.py --keywords healthy food**
   Multiple search arguments should be combined by an **AND** filter operations.
   

3. ...supports for a help function to advice users on tool usage by entering 
   **'podgen.py /help'** or ** 'podgen.py /h'** on Windows or respective
   **'podgen.py --help'** or  ** 'podgen.py --h'** on MAc/Unix.

     
4. ...displays progress and status information while the podcast is in generation.


5. ...creates an audio file (e.g. MP3), ready for direct consumption.
   Note: The audio file should be created in the current folder.


### 4. Success Criteria
A GitHub repository (public or private) that everyone can clone/download and that
directly starts up after the requirements listed in ***requirements.txt*** are fulfilled.

### 5. To get you started...
- Reading news feeds: https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm 
- Web and API development with Python: https://flask.palletsprojects.com/  
- Text to speech: https://pypi.org/project/pyttsx3/

#001 scrappingnews.py

class SiteCheck():
    """Looking for news on given website. Checking site status"""
class Downloader():
    """Downloading news  in txt"""


import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd

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

