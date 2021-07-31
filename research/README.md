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
for analytics projects. Each solution section follows the process steps of the TDSP.

Proposal:
The Task was to create a command line tool, named **podgen.py** that comes with a configuration file containing a
user-editable list of news sources to be investigated. The primary news source should be public RSS or AtomFeeds, but
additional sources are also welcome. The configuration file should contain a list of at least 30 RSS feeds from popular
news sources like CNN, NYT, FoxNews, Spiegel an others. The command line tool takes a list of comma separated keywords
or phrases arguments to used (like **Corona**; **Football**) to generate and filter the podcast. It also requires a help function to assist the user in
using the tool by entering
Do we have the help option and is it working as follows?
**'podgen.py /help'** or ** 'podgen.py /h'** on Windows or respective
**'podgen.py --help'** or  ** 'podgen.py --h'** on MAc/Unix. The commandline tool displays progress and status
information while the podcast is in generation. As result the user has different options to get the output. 
1. Read it directly with given parameters
2. Save as MP3
3. Save as PDF
Note: The audio file should be created in the current folder.

To achieve this task, we proceed according to The Team Data Science Process (TDSP). This is a standardized process model
for analytics projects. Each solution section follows the process steps of the TDSP.

### 2. Business Understanding

In the course of the task, a command line tool was created that automatically generates a podcast for the user after he
enters his interests. The podcast plays the latest interesting news for the user.

So, the **goal of the task** was to create a user-friendly tool for automatic podcast generation. The tool asks the user
for their topic preferences and generates the latest news. These news items are then read aloud by the tool. In the
process, the user can set the volume, speed and language of the podcast according to his preferences. The generated
podcast can be saved according to the user's preferences.

Proposal:
In the course of the task, a command line tool was created that automatically generates a podcast for the user after he
enters his interests. The podcast plays the latest interesting news for the user.

So, the **goal of the task** was to create a user-friendly tool for automatic podcast generation. The tool asks the user
for their topic preferences and generates the latest news. These news items are then read aloud by the tool. In the
process, the user can set the volume, speed and language of the podcast according to his preferences. The generated
podcast can be saved according to the user's preferences to an MP§ file or as PDF document. 

### 3. Data Acquisition and Understanding

#### What is an RSS Feed?
An RSS feed is an up-to-date information or list of notifications that a website delivers to its subscribers. 
RSS means "rich site summary" or "really simple syndication."

An RSS feed is read by an RSS reader or a feed reader, which can be either Web based, 
a standalone desktop application or a mobile application. 
The reader aggregates all the RSS feeds that a user is subscribed to and presents them in its UI; 
this avoids the need for the user to go to each website just to read the updates.

An RSS feed is delivered in XML format, allowing maximum compatibility between readers.
Before the advent of RSS feeds, websites sent subscribers email notifications regarding new content. 
This was not optimal, however, as some emails could end up in the junk folder or mixed with other emails, 
plus the fact that the emails are formatted differently. In contrast, an RSS reader presents all the feeds using its own interface.

#### Used Python Packages:
requests using?
pandas using?
lxml using?

pyttsx3
- Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay. 
Supports multiple TTS engines, including Sapi5, nsss, and espeak.

feedparser
- Feedparser is a Python library that parses feeds in all known formats, including. Atom, RSS, and RDF. It runs on Python 2.4 all the way up to 3.3. 

nltk using?
seaborn using?

replace
- Text processing and cleaning the output getting directly from feeds

pydub
- pydub is a Python library to work with only . wav files. By using this library we can play, split, merge, edit our . wav audio files.

art
- ASCII art is also known as "computer text art". 
It involves the smart placement of typed special characters or letters to make a visual shape that is spread over multiple lines of text.

progressbar
- A text progress bar is typically used to display the progress of a long running operation, 
providing a visual cue that processing is underway.

fpdf
- PyFPDF is a library for PDF document generation under Python, 
ported from PHP (see FPDF “Free”-PDF, a well-known PDFlib-extension replacement with many examples, scripts and derivatives).
Compared with other PDF libraries, PyFPDF is simple, small and versatile, with advanced capabilities and easy to learn, extend and maintain.

tqdm
- Instantly make your loops show a smart progress meter - just wrap any iterable with tqdm(iterable), and you’re done!


- Implementation is..

### 4. Modeling

- MP3
- Scrapper
- Key-Word
- txt-file .....

- Example:
    - Class: Converter
    - Explanation: text........


    def __init__(self, rate:int=150, volume:int=100, language:str="english"):
        self.text = ""
        self.rate = rate
        self.volume = volume
        self.language = language

        engine.setProperty('rate', self.rate)
        engine.setProperty('volume', self.volume)
        engine_voice = self.language
        if engine_voice == "english":
            voice_gender = input("Do you want a male or a female voice? (Type: male or female)")
            if voice_gender == "male":
                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
            else:
                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
        else:
            engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")

    def speak(self, text:str):
        engine.say(text)
        engine.runAndWait()

    def save_as_mp3(self, text:str, file_name:str = "podcast.mp3"):
        engine.save_to_file(text, file_name)
        engine.runAndWait()

- Learnings: text.......

1. Class: Main()
- Task: Main functionality of the app.

First part provides the design of the terminal app.

    print(text2art('''Podcast Gen''', font="small"))  # Multi-line print
    print("by Krautmacher - Ünal - Meinhold ")
    print("With this podcast generator you get an overview of the news that are interesting for you. "
      "You can either have them read to you immediately or download them for later as mp3 or pdf. ")
    print(" ")

First the PodcastGenerator will be started. With the provided Keywords from Class: Helper it will crawl through all urls inside the url list.
If the number of podcast with entries > 0 it will start the user input from Class: Help to decide the further steps. 
    
    def main():
        generator = PodcastGenerator()
        keywords = Helper.get_keyword()
        number_of_podcast = generator.generate_podcast(keywords)
        if number_of_podcast > 0:
    
If the user type in "r" it will start the reading sequence. 
    
            while True:
                read_or_save = Helper.ask_read_or_save()
                if read_or_save == "r":
                    mp3_converter = Converter()
                    mp3_converter.parameter_settings()
                    mp3_converter.speak(generator.text)
                    print("Thank you for using the Podcast Generator. We hope to see you soon!")
                    break

If the user type in "m" it will start the MP3 saving and ask for a filename. 

                if read_or_save == "m":
                    mp3_converter = Converter()
                    mp3_converter.parameter_settings()
                    mp3_file_name = Helper.ask_name_mp3()
                    mp3_converter.save_as_mp3(generator.text, f"{mp3_file_name}.mp3")
                    print("Thank you for using the Podcast Generator. We hope to see you soon!")
                    break
                    
If the user type in "p" it will start the PDF saving and ask for a filename. 
                    
                if read_or_save == "p":
                    pdf_file_name = Helper.ask_name_pdf()
                    mp3_converter = Converter()
                    mp3_converter.save_as_pdf(generator.text, f"{pdf_file_name}.pdf")
                    print("Thank you for using the Podcast Generator. We hope to see you soon!")
                    break
                else:
                    print(r"Your answer may not comply, please note that you may only press 'r', 'm' or 'p'.")
        
If no podcasts are found it will just print the following sentences. 

        
        else:
            print(f"No podcast with Keyword {keywords} found.")
    
    
    if __name__ == "__main__":
        main()
    
2. Class: PodcastGenerator()
- Task: This class provides the content from rss sites based on user given topics. It will prepare the content to a speachable format.

The Generator first splits the URL list into different sources of RSS feeds. 

    
    file = open("url_list.txt", "r")
    self.content = file.read()
    self.url_list = self.content.split(",")

get_feed_data crawls through every url inside the list and looks for the keyword ( user input: find details in Class: Helper).
If the title contains one of the keywords the summary of the article got saved in a list.
This list got cleaned to readable and necessary content. Additionally we add " New article", "Date" and " source".

        def get_feed_data(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        ticks = len(self.url_list)
        with tqdm(total=ticks, leave=False) as progress_bar:
            progress_bar.set_description("Scraping")
            counter = 0

            # rss_feed_scrapper
            for url in self.url_list:
                feed = feedparser.parse(str(url))
                # delete entries_len not in use?
                len(feed.entries)

                for entry in feed.entries:
                    for keyword in self.keywords:
                        if str(keyword) in entry.title.lower():
                            clean_summary = re.sub("(<.*?>)", "", entry.summary, 0, re.IGNORECASE | re.DOTALL |
                                                   re.MULTILINE)

                            self.feeds.append(
                                "New Article: " + feed.feed["title"] + " " + entry.published[3:17] + ", "
                                + entry.title + ". " + clean_summary)
                            self.number_of_posts += 1

                for i in range(len(self.feeds)):
                    self.feeds[i] = self.feeds[i].lower()

                counter += 0.5
                progress_bar.update(counter)
            progress_bar.update(ticks)
            print("Scraping done! Process finished: 100%")

Inside this function a progressbar was implemented to show the scrapping progress to user.

The function clean_data cleans the data for the export from noise. Noise are special characters which will disturb the speech output later.
Such characters are tags from html as well as false punctuation. As result of this class an output in txt format will be generated.

        def clean_data(self, save_to_disc: bool = False):
        """
        Cleans feed data for reading.
        :param save_to_disc: (optional) Set to True to save file to disk, otherwise False.
        :return: the cleaned text, ready for reading
        """
        feeds_clean = str(self.feeds)
        feeds_clean = feeds_clean.replace("</p>'", " ").replace("<p>", ".").replace("<h1>", " ").replace("</h1>",
                                                                                                         " ").replace(
            "</p>", " ").replace("<hr />.", " ")
        # print(feeds_clean)

        if save_to_disc:
            file = open(r'podcast.txt', 'w', encoding='utf-8')
            file.write(feeds_clean)
            file.close()

        return feeds_clean

3. Class: Helper()
- Task: Supports the main functions and gets every user input

print_help provides the manual instructions to the user when typing "h" instead of keywords 
        
    @staticmethod
    def print_help():
        """Returns the help description"""
        helper_description = "Test"
        print(helper_description)
            
get_keyword provides the user input as topics to the PodcastGenerator. Also the previous class is implented to this function. 
This will provide ther manual to the user when typing "h" instead of any topic. 
After the user typed in his keywords, this function will split all inputs with "," to prepare them for crawling through feeds.

    @staticmethod
    def get_keyword():
        keyword = str(input("To start enter one or more comma separated topics (eg: corona, soccer, germany) or enter "
                            "'h' to get an introduction into the program"))
        if keyword == "h":
            Helper.print_help()
            keyword = str(input("To start enter one or more comma separated topics (eg: corona, soccer, germany)"))
            keywords = keyword.lower().split(",")
            print(f"Given topics are {keywords}")
            return keywords
        else:
            keywords = keyword.lower().split(",")
            print(f"Given topics are {keywords}")
            return keywords

    
Following functions will ask the user fo his parameters used inside speech part. These paramters can be saved and automatically used for the next run. 
Paramters can be:

- Voice rate 
- Voice volume
- Voice language ( at this moment only german and english )
- Voice gender

You will also find the questions for reading or saving in MP3 or PDF in this part

    @staticmethod
    def ask_parameters():
       return input(
         "Would you like to use the default settings (voice rate, language, volume) for the Podcast? (Type 'y' for "
         "yes or 'n' for no.)")

    @staticmethod
    def get_voice_rate():
        return input("Please select a voice rate between 100 and 200 (Recommendation = 150).")

    @staticmethod
    def get_voice_volume():
        return input("Please select the volume between 0 and 1.0 (Recommendation = 1.0).")

    @staticmethod
    def get_voice_language():
        return input("Please select german or english as language (Type 'g' for german or 'e' for english).")

    @staticmethod
    def get_voice_gender():
        return input("Please select the speakers gender (Type 'm' for male or 'f' for female).")

    @staticmethod
    def ask_to_save_parameter():
        return input(
            "Do you like to save the parameter you have entered as new standard parameters for the next time? (y/n)")

    @staticmethod
    def ask_read_or_save():
        return input(
            "Please select whether you want the podcast to be read aloud (r) now, saved as an mp3 (m) for later, "
            "or saved as a pdf (p) for later (r/m/p).")

    @staticmethod
    def ask_name_mp3():
        return input("What name should the mp3-file have? (Please do not type '.mp3' after the name)")

    @staticmethod
    def ask_name_pdf():
        return input("What name should the pdf-file have? (Please do not type '.pdf' after the name)")

1. Class: Converter()
- Task: The Converter class includes the functions to read out the podcast, save it as mp3 and save it as pdf. Also, the class includes the setting of the speed, the rate and the language of the podcast. 
- Functions:
  - def init: The init function initiates the class and sets the parameters (volume, rate and speech). 
  - def speak: The speak function reads out the podcast with the previously set parameters.  
  - def save_as_mp3: 
    - Code:
      ```
        text = text.replace(".", ", ")
        engine.save_to_file(text, file_name)
        engine.runAndWait()
      ```
    - The save_as_mp3 function saves the podcast as an mp3 file on the user's disk so that the user can access it offline. 
    - Problem: While creating the mp3 file, the problem appeared that the mp3 was stopped after the first dot. We fixed this by replacing all the dots with commas.This still leaves a pause when speaking and the text is read aloud completely.
  - def save_as_pdf: 
    - The save_as_pdf function saves the podcast as a pdf file to the user's hard disk so that the user can read it offline.
    - Problem: It is problematic to save the text as utf-8, because it contains special characters that can only be captured by latin-1 (uses the fpdf package). So text has to be encoded in latin-q beforehand
    - Code:
      ```
        text_encoded = text.encode('latin-1', 'replace').decode('latin-1')
        text = text_encoded.replace("?", ".").replace("[", "").replace("]", "").replace("'", "")

        a4_width_mm = 210
        pt_to_mm = 0.35
        fontsize_pt = 10
        fontsize_mm = fontsize_pt * pt_to_mm
        margin_bottom_mm = 10
        character_width_mm = 7 * pt_to_mm
        width_text = a4_width_mm / character_width_mm

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_auto_page_break(True, margin=margin_bottom_mm)
        pdf.add_page()
        pdf.set_font(family='Courier', size=fontsize_pt)
        splitted = text.split('\n')

        for line in splitted:
            lines = textwrap.wrap(line, width_text)

            if len(lines) == 0:
                pdf.ln()

            for wrap in lines:
                pdf.cell(0, fontsize_mm, wrap, ln=1)

            pdf.output(file_name, 'F')
            print(text)```
- Learnings:

```
shell
```

### 5. Achievements

- Summary, if the target have been archived

#### What are the optimization potentials of the program? What were problems?
One big problem was the letter structur of the user input. "Corona" should be the same as "corona".
Actually these words are not the same while working with python. 
So we implement the transformation of every word in small letters. For the PDF file we had to use another output because for reading it is necessary to get capital letters also. 

Also the cleaning part for the speaking was a big problem we had to deal with. Code loaded directly from rss page is full of tags and special characters, also called noise.
We had to clean everything except the part we really needed for the speaking, writing or MP3 output. 


There are also some topics we would like to implement in future: 

1. User input
- check for synonyms for the user input
- Make recommendations for keywords to search for 
- Possibility to look for given topics 

2. Set options in application 
- enter save path for the MP3 and PDF file
- enter url to extend the url list

3. Output
- only show new entries
- nice formatting inside PDF file 


### 6. Display the Process

Example:
![img.png](img.png)

### Outlook future/ Reference

> enjoy your individual podcasts!