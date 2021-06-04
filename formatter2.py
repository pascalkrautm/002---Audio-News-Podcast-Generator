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
import os

rssfeed = 'https://rss.sueddeutsche.de/rss/Topthemen'
parsethefeed = feedparser.parse(rssfeed)

df = pd.DataFrame()

df['title'] = [post.title for post in parsethefeed.entries]
df['summary'] = [post.summary for post in parsethefeed.entries]
print(df)
df.head
df.describe()

df_clean = df.replace("<img alt=", "")
df_clean = df_clean.replace(":", "")
df_clean = df_clean.replace(".", "")
df_clean = df_clean.replace("/><p>", "")
df_clean = df_clean.replace(".</p>", "")
df_clean = df_clean.replace("***", "")
df_clean = df_clean.replace("src=", "")
print(df_clean)

df_clean.to_csv('myfilename5.csv', header=None, index=None, sep=' ', mode='a')





# To be clarified:
# How can I use the filtered data from the scrapper?