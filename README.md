- Pascal Krautmacher [697450]
- Marco Alexander Meinhold [872406]
- Eren Ünal [859039]

The following markdown code would create a valid output. Only Pascal Krautmacher, Marco Alexander Meinhold and Eren Ünal
will evaluted for the use case.

# 002---Audio-News-Podcast-Generator

**002 - Audio News Podcast Generator, MBA HSD SS21**

**Summary**: Automated generation of a podcast from relevant news available on the internet.

### Team

#### Project Lead:

- Thomas Zeutschler

#### Data Scientist:

- Pascal Krautmacher
- Marco Alexander Meinhold
- Eren Ünal

### 1. Task

The Task was to create a command line tool, named **podgen.py** that comes with a configuration file containing a
user-editable list of news sources to be investigated. The primary news source should be public RSS or AtomFeeds, but
additional sources are also welcome. The configuration file should contain a list of at least 30 RSS feeds from popular
news sources like CNN, NYT, FoxNews, Spiegel an others. The command line tool takes a list of comma separated keywords
or phrases arguments to used (like **Corona**; **Football**) to generate and filter the podcast. Multiple search
arguments should be combined by an **AND** filter operations. It also requires a help function to assist the user in
using the tool by entering
**'podgen.py /help'** or ** 'podgen.py /h'** on Windows or respective
**'podgen.py --help'** or  ** 'podgen.py --h'** on MAc/Unix. The commandline tool displays progress and status
information while the podcast is in generation. At least, the command line tool reates an audio file (e.g. MP3), ready
for direct consumption. Note: The audio file should be created in the current folder.

To achieve this task, we proceed according to The Team Data Science Process (TDSP). This is a standardized process model
for analytics projects. Each solution section follows the process steps of the TDSP

### 2. Business Understanding

Understand and Questions

### 3. Data Acquisition and Understanding

-Which Packages used?

-Scrapper, Key word and txt-File

-Display codes as follows:

    def url_list(self):
        content = open("url_list.txt", "r")
        content = content.read()
        url_list = content.split(",")
    return url_list(

### 4. Modeling

MP3

### 5. Deployment

What are the optimization potentials of the program? What were the problems?

### 6. Display the Process

**Me:** *I'm so bored, please read out something interesting to me.*

**You:** *No problem, I'm a Python hero!*

#

> enjoy your individual podcasts!