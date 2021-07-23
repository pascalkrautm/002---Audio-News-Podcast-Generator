import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
#from pydub import AudioSegment
import pyttsx3
import feedparser
import ssl
import re
from art import *

rt = text2art("Podcast Gen",font='block',chr_ignore=True) # Return ASCII text with block font
print(rt)
ssl._create_default_https_context = ssl._create_unverified_context

xml_list = []
article_list = []
feeds = []

#url_list
content = open("url_list.txt", "r")
content = content.read()
url_list = content.split(",")
print(url_list)
#User input
keyword = input("What topic are you interested in? Just type 'keyword' ('corona', 'soccer')")

#liste leeren
del feeds[:]

#rss_feed_scrapper
for url in url_list:
    feed = feedparser.parse(str(url))
    print("Starting scrap " + str(url))
    entries_len = len(feed.entries)
    print(f"getting {entries_len} entries")
    print("searching for keyword")
    #print(feed.entries)
    for entry in feed.entries:
        if keyword in entry.title:
            #testline
            #print(entry.title)
            #testline
            #print(entry.summary)
            #print(entry.published)
            clean_summary = re.sub("(<img.*?>)", "", entry.summary, 0, re.IGNORECASE | re.DOTALL | re.MULTILINE)
            feeds.append("Neuer Artikel: " + feed.feed["title"] + " " + entry.published[3:17] + ", " + entry.title
                         + clean_summary)
        else:
            pass


feeds_clean = str(feeds)
feeds_clean_new = feeds_clean.replace("</p>'", " ")
feeds_clean_new1 = feeds_clean_new.replace("<p>", ".")
print(feeds_clean_new1)

myText = open(r'podcast.txt', 'w', encoding='utf-8')
myString = feeds_clean_new1
myText.write(myString)
myText.close()
print(myText)

engine = pyttsx3.init()

en_voice_male_id = "com.apple.speech.synthesis.voice.Alex"
en_voice_female_id = "com.apple.speech.synthesis.voice.Victoria"
us_voice_male_id = "com.apple.speech.synthesis.voice.Fred"
de_voice_female_id = "com.apple.speech.synthesis.voice.anna.premium"
voice = engine.getProperty('voice')

engine_voice = input("Which language do you want? (Type: english or german)")
if engine_voice == "english":
    voice_gender = input("Do you want a male or a female voice? (Type: male or female)")
    if voice_gender == "male":
        engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
    else:
        engine.setProperty('voice', en_voice_female_id)
else:
    engine.setProperty('voice', de_voice_female_id)

engine.setProperty('volume', "5.0")
voice = engine.getProperty('voice')
engine.setProperty('rate', 150)

with open("podcast.txt") as file:
   file = file.read()

engine.say(file)

#sound = AudioSegment.from_file(file)
#sound.export("Podcast", format="mp3", bitrate="128k")

engine.runAndWait()