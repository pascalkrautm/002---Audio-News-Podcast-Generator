import re

class Formatter(object): #format feedparser output to a readable text file
    def load_feedparseroutput(self):
        feedsnew = self
        return feedsnew

    def convert_intostring(self):
        feedsnew= str.(self)
        return feedsnew

    def clean_string (self):
        feeds_clean = str(re.findall("<p>(.*?)</p>", feeds_new, re.DOTALL))
        return feeds_clean

    def save_astxt(self):
        myText = open(r'Feedoutputformp3.txt', 'w')
        myString = feeds_clean
        myText.write(myString)
        myText.close()
        return myText.Close()

