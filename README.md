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

# requirements txt is uploaded 

# 001 scrappingnews.py

we’re going to call the Requests library and fetch our website using requests.get(...). 
Printing the status code to the terminal using r.status_code to check that the website has been successfully called.
Additionally, I’ve wrapped this into a try: except: to catch any errors we may have later on down the road.
Once we run the program, we’ll see a successful status code of 200. This states that we’re able to ping the site and “get” information.

scraping function:

def url_opener(url):
    print("Starting scraping" + str(url))
    try:
        r = requests.get(url)
        return print("Finished scraping" + str(url) + "with: ", r.status_code)
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)


