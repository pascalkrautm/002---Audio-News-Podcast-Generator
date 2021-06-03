
import feedparser
import pandas as pd

rssfeed = 'https://rss.sueddeutsche.de/rss/Topthemen'
parsethefeed = feedparser.parse(rssfeed)

df = pd.DataFrame()

df['title'] = [post.title for post in parsethefeed.entries]
df['description'] = [post.description for post in parsethefeed.entries]
df['link'] = [post.link for post in parsethefeed.entries]
print(df)

df.to_csv('myfilename.csv', index=False)
