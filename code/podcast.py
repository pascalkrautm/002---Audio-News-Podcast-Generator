import re

class Podcast:
    def __init__(self,feeds_new:str):
        self.feeds_new = feeds_new
        self.feeds_clean = []
        self.myText = mytext
        self.myString = mystring

    def clean(self):
        self.feeds_new = str(self.feeds)
        feeds_clean = str(re.findall("<p>(.*?)</p>", self.feeds_new, re.DOTALL))
        print(feeds_clean)

        return self.feeds_clean

    def saver(self):
        mytext = open(r'Feedoutputformp3.txt', 'w')
        mystring = self.feeds_clean
        mytext.write(mystring)
        mytext.close()

        return mytext.close()