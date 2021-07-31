- Pascal Krautmacher [697450]
- Marco Alexander Meinhold [872406]
- Eren Ünal [859039]

The following Markdown code would create a valid output. Only Pascal Krautmacher, Marco Alexander Meinhold and Eren Ünal
will evaluate for the use case.

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

![img.png](docs/Cover page.png)

***
### Table of Contents
1. [Task](#1-task)
2. [Business Understanding](#2-business-understanding)
3. [Data Acquisition and Understanding](#3-data-acquisition-and-understanding)
4. [Modeling](#4-modeling)
5. [Achievements](#5-achievements)
6. [Display the Process](#6-display-the-process)
7. [Outlook/Reference ](#7-outlookreference)
***
### Installation

A little intro about the installation. 
```
$ git clone https://github.com/pascalkrautm/002---Audio-News-Podcast-Generator.git
$ cd ../path/to/the/file
$ npm install
$ npm start
```
Side information: To use the application in a special environment use ```lorem ipsum```
***

### 1. Task

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
***

### 2. Business Understanding
In the course of the task, a command line tool was created that automatically generates a podcast for the user after he
enters his interests. The podcast plays the latest interesting news for the user.

So, the **goal of the task** was to create a user-friendly tool for automatic podcast generation. The tool asks the user
for their topic preferences and generates the latest news. These news items are then read aloud by the tool. In the
process, the user can set the volume, speed and language of the podcast according to his preferences. The generated
podcast can be saved according to the user's preferences to an MP§ file or as PDF document. 

### 3. Data Acquisition and Understanding

#### What is an RSS Feed?
An RSS feed is up-to-date information or list of notifications that a website delivers to its subscribers. 
RSS means "rich site summary" or "really simple syndication."

An RSS feed is read by an RSS reader or a feed reader, which can be either Web based, 
a standalone desktop application or a mobile application. 
The reader aggregates all the RSS feeds that a user is subscribed to and presents them in its UI; 
this avoids the need for the user to go to each website just to read the updates.

An RSS feed is delivered in XML format, allowing maximum compatibility between readers.
Before the advent of RSS feeds, websites sent subscribers email notifications regarding new content. 
This was not optimal, however, as some emails could end up in the junk folder or mixed with other emails, 
plus the fact that the emails are formatted differently. In contrast, an RSS reader presents all the feeds using its o
wn interface.

#### What is an XML-File?
RSS is based, as already mentioned, on an XML file. An XML file, which is an extensible markup language file, is used 
to structure data for the purpose of storage and transport. An XML file consists of tags such as `<title>` and the 
text behind it. The tags are used to reflect the data structure while the text is to be stored. The texts in an XML file 
are surrounded by tags, which must correspond to different syntax guidelines. The bottom line is that the XML file is a 
text file with user-defined tags that describe the document structure and specify how the data is to be stored and 
transported.

<ins>For example, an XML file looks like this:</ins>
![img_1.png](docs/Example_of_XML-File.png)
In this example we have the <channel> tag, which contains several sub-elements or tags.

The tags are listed and explained below:
  - title = channel name of the rss feed
  - link = URL of the channel/ HTML website
  - description = describe the channel
  - language = the language of the channel. In this case, the information on the channel is in English, as 'en-us'.
  - pubDate = date on which the content was published 
  - lastBuildDate = last day on which the content was updated
  - docs = Reference to the used documentation format of the RSS file by the URL
  - generator = a string indicating the program used to generate the channel
  - managingEditor = email address for person responsible for editorial content
  - Webmaster = email address for person responsible for technical issues relating to channel
  - item
    - title = the title of the item
    - link = the URL of the item
    - description = The description of the item
    - pubDate = indicates when the item was published
    - guid = a string that uniquely identifies the item
    
As part of the scraper, the desired tags are given as arguments, so that only the text behind the respective tag is 
filtered out of the XML file. For more detailed information see chapter 4.
#### Used Python Packages:
The used packages are all already listed in the requirements and only need to be installed. For ease of reference, however, these are listed separately and briefly explained in the following. If you click on the respective package, you will be automatically redirected to the documentation of the respective package. 

See: [requirements](code/requirements.txt)

[pyttsx3](https://pypi.org/project/pyttsx3/)
- Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay. 
Supports multiple TTS engines, including Sapi5, nsss, and espeak.

[feedparser](https://pypi.org/project/feedparser/)
- Feedparser is a Python library that parses feeds in all known formats, including. Atom, RSS, and RDF. It runs on Python 2.4 all the way up to 3.3.

[replace](https://pypi.org/project/replace/)
- Text processing and cleaning the output getting directly from feeds

[pydub](https://pypi.org/project/pydub/)
- pydub is a Python library to work with only . wav files. By using this library we can play, split, merge, edit our . wav audio files.

[art](https://pypi.org/project/art/)
- ASCII art is also known as "computer text art". 
It involves the smart placement of typed special characters or letters to make a visual shape that is spread over multiple lines of text.

[progressbar](https://pypi.org/project/progressbar/)
- A text progress bar is typically used to display the progress of a long-running operation, 
providing a visual cue that processing is underway.

[fpdf](https://pypi.org/project/fpdf/)
- PyFPDF is a library for PDF document generation under Python, 
ported from PHP (see FPDF “Free”-PDF, a well-known PDFlib-extension replacement with many examples, scripts and derivatives).
Compared with other PDF libraries, PyFPDF is simple, small and versatile, with advanced capabilities and easy to learn, extend and maintain.

[tqdm](https://pypi.org/project/tqdm/)
- Instantly make your loops show a smart progress meter - just wrap any iterable with tqdm(iterable), and you’re done!


- Implementation is.#What do we want to say here?
***

### 4. Modeling
By executing the [main](code/main.py) you can start with the podcast generator. Nevertheless, in the following all classes are briefly listed and the essential explanation aspects are highlighted 

<ins>1. Class: **Main()**
- <ins>Task</ins>: Main functionality of the app.

First part provides the design of the terminal app. The aim here is to make the Commandline tool more user-friendly

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
    
If the podcasts with entries > 0, the user is first asked if he wants to have the entries read aloud or if he wants to save it as pdf or as mp3 to be able to refer to it in a later time course

If the user enters "r" and thus selects the reading out of the entries, the reading sequence is started. 
    
            while True:
                read_or_save = Helper.ask_read_or_save()
                if read_or_save == "r":
                    mp3_converter = Converter()
                    mp3_converter.parameter_settings()
                    mp3_converter.speak(generator.text)
                    print("Thank you for using the Podcast Generator. We hope to see you soon!")
                    break

If, on the other hand, the user selects "m" and thus saves as mp3, mp3 saving is started and a file name is requested. 

                if read_or_save == "m":
                    mp3_converter = Converter()
                    mp3_converter.parameter_settings()
                    mp3_file_name = Helper.ask_name_mp3()
                    mp3_converter.save_as_mp3(generator.text, f"{mp3_file_name}.mp3")
                    print("Thank you for using the Podcast Generator. We hope to see you soon!")
                    break
                    
If the user types "p" to select save as PDF, the PDF saving will start and ask for a file name. 
                    
                if read_or_save == "p":
                    pdf_file_name = Helper.ask_name_pdf()
                    mp3_converter = Converter()
                    mp3_converter.save_as_pdf(generator.text, f"{pdf_file_name}.pdf")
                    print("Thank you for using the Podcast Generator. We hope to see you soon!")
                    break
                else:
                    print(r"Your answer may not comply, please note that you may only press 'r', 'm' or 'p'.")
        
If no podcasts are found, only the following records will be printed. The user must manually restart or run the process 
at this point

        else:
            print(f"No podcast with Keyword {keywords} found.")
    
    
    if __name__ == "__main__":
        main()
    
<ins>2. Class: **PodcastGenerator()**
- <ins>Task</ins>: This class provides the content of RSS pages based on user-defined topics. It searches the XML files for appropriate information and prepares the content in a searchable format. 

The generator first divides the URL list into different sources of RSS feeds. Our URL list includes well-known newsletters such as BBC, Skynews, Yahoo, CNN, NYT, FoxNews and others. The list can be found here: [url_list](code/url_list.txt)

    file = open("url_list.txt", "r")
    self.content = file.read()
    self.url_list = self.content.split(",")

get_feed_data scans every URL in the list and searches for the keyword (user input: find details in Class: Helper).
If the title contains one of the keywords, the summary of the article is stored in a list.
This list is adjusted for readable and necessary content. We go there and pull out only the pure text in the respective day. This means, for example, that we extract only the plain text from the tags `<summary>` or `<published>` and remove the special characters. In addition, we add “New Item”, “Date” and “Source” to ensure clarity

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

3. <ins>Class: **Helper()**
- <ins>Task</ins>: Supports the main functions and gets every user input

print_help provides the user with the manual instructions when he enters “h” instead of keywords. The manual instructions are listed together using a For loop to provide users with better clarity
        
    @staticmethod
        def print_help():
        """Returns the help description"""
        helper_description = ("To generate the RSS feed, you need to answer several questions."
                              "Below are these questions with their purpose for clarification and understanding:",
                              "-In the first step you need to enter your desired topics so that the present program"
                              " can search the Internet according to your entered interests",
                              "-You will then be asked whether you want the news to be generated as a pdf, mp3 or"
                              " voice-speak. If you choose the pdf or mp3 variant, please note that the result will"
                              " be saved in the 'data' folder. If you decide for pdf, there is nothing more to do in "
                              " the following.",
                              "-If you use the mp3 or voice-speak variant there are further questions to consider"
                              " You have to set the voice rate, language and volume for your output."
                              " You will be asked if you want to use the default settings."
                              " Note: When you start the program for the first time, these settings are not yet"
                              " available, so you have to define the parameters once. You can change the parameters"
                              " at any time at this point")
        for value in helper_description:
            print(value)
            
get_keyword provides the user input as topics to the PodcastGenerator. Also, the previous class is implemented to this function. 
This will provide there manual to the user when typing "h" instead of any topic. 
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

    
Following functions will ask the user fo his parameters used inside speech part. These parameters can be saved and automatically used for the next run. Please note that in the first run of the program there are no parameters for the system, so that the system works here with the parameters we preset, unless any information is given 
Parameters can be:

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

4. <ins>Class: **Converter()**
- <ins>Task</ins>: Supports the main functions. The Converter class includes the functions to read out the podcast, save it as mp3 and save it as pdf. Also, the class includes the setting of the speed, the rate and the language of the podcast.

With parameter_settings () the user’s information is taken into account in the program. If the user indicates that he does not want to use the preset parameters, the resulting queries are managed here. Several while loops have been coded here to warn the user that the program is unable to process it in the event of an incorrect entry. At this point, however, the user is again asked to enter the information correct
        
    def parameter_settings(self):
        while True:
            engine_parameters = Helper.ask_parameters()
            if engine_parameters == "n":
                self.rate = Helper.get_voice_rate()
                engine.setProperty('rate', self.rate)
                self.volume = Helper.get_voice_volume()
                engine.setProperty('volume', self.volume)
                while True:
                    self.language = Helper.get_voice_language()
                    if self.language == "e":
                        while True:
                            self.gender = Helper.get_voice_gender()
                            if self.gender == "m":
                                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
                                break
                            if self.gender == "f":
                                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
                                break
                            else:
                                print(r"Your answer may not comply, please note that you may only press 'm' or 'f'")
                        break
                    if self.language == "g":
                        engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")
                        break
                    else:
                        print(r"Your answer may not comply, please note that you may only press 'g' or 'e'")
                while True:
                    engine_save_parameter = Helper.ask_to_save_parameter()
                    if engine_save_parameter == "y":
                        # create a list with our default parameters
                        save_parameters = [self.rate, self.volume, self.language, self.gender]
                        # save our list for next session
                        open_file = open("parameters.pkl", "wb")
                        pickle.dump(save_parameters, open_file)
                        open_file.close()
                        break
                    if engine_save_parameter == "n":
                        pass
                        break
                    else:
                        print(r"Your answer may not comply, please note that you may only press 'y' or 'n'")
                break

However, this definition also takes into account the case when the user wants to work with the preset parameters. Several while loops have been coded here to warn the user that the program is unable to process it in the event of an incorrect entry. At this point, however, the user is again asked to enter the information correct

            if engine_parameters == "y":
                # load saved parameters from last session
                open_file = open("parameters.pkl", "rb")
                parameter_list = pickle.load(open_file)
                open_file.close()
                voice_rate_default = parameter_list[0]
                voice_volume_default = parameter_list[1]
                voice_language_default = parameter_list[2]
                voice_gender_default = parameter_list[3]
                engine.setProperty('rate', voice_rate_default)
                engine.setProperty('volume', voice_volume_default)
                if voice_language_default == "e":
                    if voice_gender_default == "m":
                        engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
                    if voice_gender_default == "f":
                        engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
                if self.language == "g":
                    engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")

                engine.setProperty('language', voice_language_default)
                break
            else:
                print(r"Your answer may not comply, please note that you may only press 'y' or 'n'")

With speak() the commandline reads out the podcast with the previously set parameters.  

    def speak(self, text: str):
        engine.say(text)
        engine.runAndWait()

The save_as_mp3 function saves the podcast as a mp3 file on the user's disk so that the user can access it offline. 
_Problem:_  While creating the mp3 file, the problem appeared that the mp3 was stopped after the first dot. We fixed this by replacing all the dots with commas.This still leaves a pause when speaking and the text is read aloud completely.

    def save_as_mp3(self, text: str, file_name: str = "podcast.mp3"):
        text = text.replace(".", ", ")
        engine.save_to_file(text, file_name)
        engine.runAndWait()

The save_as_pdf function saves the podcast as a pdf file, so that the user can access it offline. 
_Problem:_ It is problematic to save the text as utf-8, because it contains special characters that can only be captured by latin-1 (uses the fpdf package). So text has to be encoded in latin-q beforehand. Another problem was that when the pdf file was created, a paragraph was made for each letter in the pdf file. We solved the problem by splitting the feed entries beforehand with `('\n')` and then using a for loop to apply the module [textwrap.wrap](https://docs.python.org/3/library/textwrap.html) to all entries.

    def save_as_pdf(self, text: str, file_name: str = "Podcast.pdf"):
        text_encoded = text.encode('latin-1', 'replace').decode('latin-1')
        text = text_encoded.replace("?", ".").replace("[", "").replace("]", "").replace("'", "")

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_auto_page_break(True, margin=10)
        pdf.add_page()
        pdf.set_font(family='Courier', size=12)
        splitter = text.split('\n')

        for line in splitter:
            lines = textwrap.wrap(line, 75)
            if len(lines) == 0:
                pdf.ln()
            for wrap in lines:
                pdf.cell(0, 4, wrap, ln=1)
            pdf.output(file_name, 'F')


- Learnings:

### 5. Achievements

- Summary, if the target have been archived

#### What are the optimization potentials of the program? What were problems?
One big problem was the letter structure of the user input. "Corona" should be the same as "corona".
Actually these words are not the same while working with python. 
So we implement the transformation of every word in small letters. For the PDF file we had to use another output because for reading it is necessary to get capital letters also. 

Also, the cleaning part for the speaking was a big problem we had to deal with. Code loaded directly from rss page is full of tags and special characters, also called noise.
We had to clean everything except the part we really needed for the speaking, writing or MP3 output. 


There are also some topics we would like to implement in the future: 

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
***

### 6. Display the Process

***
### 7. Outlook/Reference 
- Coming soon