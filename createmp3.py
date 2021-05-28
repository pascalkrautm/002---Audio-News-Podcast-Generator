import pyttsx3

class Converter(Object): #Create class for the Object "Converter"
    def __init__(self):
        self.file_name = file_name
        self.text = text
        self.rate = rate
        self.volume = volume
        self. voices = voices

    def rate_option(self):
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        engine.setProperty('rate', 125) # setting up new voice rate

    def volume_option(self):
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        print(volume)  # printing current volume level
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    def voice_option(self):
        voices = engine.getProperty('voices')  # getting details of current voice
        engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

    def saving_mp3(self):
        engine.save_to_file('Hello World', 'test.mp3')
        engine.runAndWait()

#Noch zu verarbeiten
engine = pyttsx3.init() # object creation

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()


#Auszug aus dem Buch
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()