class Formatter(object): #Create dataframe and convert it to txt
    def __init__(self):
        self.rssfeed = link
        #self.parsefeed = parsefeed
        #self.df = df

    def parse_rssfeed(self):
        rssfeed = link #getting the rss feed
        parsefeed = feedparser.parse(rssfeed) #parse the rss feed
        print(parsefeed)

    def formate_intodataframe(self):
        df = pd.DataFrame() #formate the parse output in a dataframe
        df['title'] = [post.title for post in parsefeed.entries]
        df['description'] = [post.description for post in parsefeed.entries]
        df['link'] = [post.link for post in parsefeed.entries]
        print(df)

    def convert_intotxt (self):
        df.to_csv('myfilename.txt', header=None, index=None, sep=' ', mode='a') #write content of DataFrame into text file

    def clean_txt(self):
        pass

#Test:
import feedparser
import pandas as pd
import numpy as np

rssfeed = 'https://rss.sueddeutsche.de/rss/Topthemen'
parsethefeed = feedparser.parse(rssfeed)

df = pd.DataFrame()

df['title'] = [post.title for post in parsethefeed.entries]
df['description'] = [post.description for post in parsethefeed.entries]
df['link'] = [post.link for post in parsethefeed.entries]
print(df)

df_cleaned = df.replace(":", "")
print(df_cleaned)

df.to_csv('myfilename.txt', header=None, index=None, sep=' ', mode='a')
df.to_csv(r'myfilename2.txt', header=None, index=None, sep='\t', mode='a')
df_cleaned.to_csv(r'myfilename3.txt', header=None, index=None, sep='\t', mode='a')

filename = 'myfilename.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words by white space
words = text.split()
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped[:100])

import nltk
nltk.download()

# load data
filename = 'myfilename.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])


# To be clarified:
# How can I use the filtered data from the scrapper?