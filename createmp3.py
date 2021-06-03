import pyttsx3

engine = pyttsx3.init()

class Converter(object): #Create class for the Object "Converter"
    def __init__(self, file_name, text, rate, volume, voice):
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

    def speak(self):
        engine.say("Hello World")
        engine.runAndWait()

    def saving_mp3(self):
        engine.save_to_file('Hello World', 'test.mp3')
        engine.runAndWait()


