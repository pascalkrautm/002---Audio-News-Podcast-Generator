- Pascal Krautmacher [697450]
- Marco Alexander Meinhold [872406]
- Eren Ünal [859039]

The following markdown code would create a valid output. Only Pascal Krautmacher, Marco Alexander Meinhold and Eren Ünal
will evaluted for the use case.

# 002---Audio-News-Podcast-Generator
**002 - Audio News Podcast Generator, MBA HSD SS21**

**Summary**: Automated generation of a podcast from relevant news
available on the internet.

###Team
####Project Lead: 
- Thomas Zeutschler

####Data Scientist:
- Pascal Krautmacher
- Marco Alexander Meinhold
- Eren Ünal

###1. Task
The Task was to create a command line tool, named **podgen.py** that comes with a configuration file containing a user-editable list of news 
sources to be investigated. The primary news source should be public 
RSS or AtomFeeds, but additional sources are also welcome. The configuration file should contain a list of at least 30 RSS feeds
from popular news sources like CNN, NYT, FoxNews, Spiegel an others. The command line tool takes a list of comma separated keywords or phrases arguments to used (like **Corona**; **Football**) to generate and filter the podcast. Multiple search arguments should be combined by an **AND** filter operations. 
It also requires a help function to assist the user in using the tool by entering
**'podgen.py /help'** or ** 'podgen.py /h'** on Windows or respective
**'podgen.py --help'** or  ** 'podgen.py --h'** on MAc/Unix. 
The commandline tool displays progress and status information while the podcast is in generation.
At least, the command line tool reates an audio file (e.g. MP3), ready for direct consumption.
Note: The audio file should be created in the current folder.

To achieve this task, we proceed according to The Team Data Science Process (TDSP). This is a standardized process model for analytics projects. Each solution section follows the process steps of the TDSP

###2. Business Understanding
Understand and Questions 

###3. Data Acquisition and Understanding
Key word and txt-File

###4. Modeling
MP3

###5. Deployment

###6. Display the Process 


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

# Process
## class Url_list
- import url list from url_list.txt
- formats all urls to readable url for code
- all urls linking to different rss feeds

## class Keyword_provider
- uses User Input as searching parameter for rss feed content
- should be executed via podgen.py --keyowrds example1, example2

## class Rss_feed_scrapper
- looping through all given urls from Class Url_list
- searching for given keyword from Class Keyword_provider in titles from rss feed
- saving all descriptions when keyword was found in title
- Return list with all needed descriptions

## class list_formatter
- formats all list parameter to text only 

## class text_exporter
- exports list with formatted text to txt file

## class mp3_converter
- converts text from class text_exporter to one mp3 file

## class help
- podgen --help provides a help files with manual for the generator

> enjoy your individual podcasts!

# Installing apps for the job 

bs4
requests
pandas
lxml
pytts3
feedparser

# Import

import pandas as pd
import requests
import feedparser
import ssl

# 001 ree_feed_scrapper.py

First we need to get several informations to fulfill our job. Important information are the url list from where we will get our sources. Url_list.py will import our sources and fomrats them to readable format for our app. 
Feel free to extend the list on your own in Url_list.txt. The format has to be like (comma seperated: 
https://rss.sueddeutsche.de/rss/Topthemen,https://www.haz.de/rss/feed/haz_schlagzeilen,https://www.duesseldorf.de/index.php?id=700027212&type=1457698658

    def url_list(self):
        content = open("url_list.txt", "r")
        content = content.read()
        url_list = content.split(",")
    return url_list()

Then we need the user input declared as our keyword. This keyword is the topic for our scrapping job. 
In Keyword_provider.py we will ask the user for topics, he want to get new info for. This input should be provided in one word like Corona, Soccer etc.
(disregard capital letters)

   keyword = input("What topic are you interested in? Just type 'keyword' ('corona', 'soccer')")

The rss_feed_scrapper will do the main job in scrapping our relevant information. 
Via feedparser it will go through every url from Url_list.py and look for the keyword in "title". Inside a loop it will append the "summary" realting to that title inside a list feeds[]. If the keyword ist not found, it will pass. 

   for url in url_list:
      feed = feedparser.parse(str(url))
      print("Starting scrap " + str(url))
      entries_len = len(feed.entries)
      print(f"getting {entries_len} entries")
      print("searching for keyword")
      for entry in feed.entries:
         if keyword in entry.title:
               #testline
               print(entry.title)
               #testline
               print(entry.summary)
               feeds.append(entry.summary)
         else:
               pass


for a new run we need to clean our list feeds[] via 

del feeds[:]

For disregarding http or https we need to add the following to our code:

ssl._create_default_https_context = ssl._create_unverified_context

We will get a list with all summarys for our given topic. The output looks as follows:

['<img alt="Coronavirus - Bayern" src="https://www.sueddeutsche.de/image/sz.1.5310784/208x156" /><p>Am Dienstag hatte er bayernweit bei 35,6 gelegen. Mindestens zwei Verdachtsfälle von Unregelmäßigkeiten in Testzentren.</p>', '<img alt="Stiko-Vorsitzender Mertens" src="https://www.sueddeutsche.de/image/sz.1.5310782/208x156" /><p>In einem Interview wirbt Mertens um Verständnis für die zögerliche Haltung der Ständigen Impfkommission bei Kinderimpfungen gegen Corona. Die bundesweite Inzidenz steigt dem RKI zufolge auf 36,8.</p>', 'Digitales Pressegespräch zur Corona-Pandemie mit Oberbürgermeister Dr. Keller und Stadtdirektor Hintzsche']

