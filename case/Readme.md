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

