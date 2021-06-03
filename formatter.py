class Formatter(object): #Create a cleaned dataframe and convert it to txt
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
        df.to_csv('myfilename.csv', header=None, index=None, sep=' ', mode='a') #write content of DataFrame into text File

    def clean_txt(self):
        pass

