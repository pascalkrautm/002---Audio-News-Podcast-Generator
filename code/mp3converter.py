import pyttsx3
import fpdf
from fpdf import FPDF

from helper import Helper

engine = pyttsx3.init()

class Converter(object): #Create class for the Object "Converter"
    def __init__(self, rate:int=150, volume:int=100, language:str="english"):
        self.text = ""
        self.rate = rate
        self.volume = volume
        self.language = language

        engine.setProperty('rate', self.rate)

        engine.setProperty('volume', self.volume)

        engine_voice = self.language
        if engine_voice == "e":
            voice_gender = Helper.get_voice_gender()
            if voice_gender == "m":
                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
            else:
                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
        if engine_voice== "g":
            engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")

    def speak(self, text:str):
        engine.say(text)
        engine.runAndWait()

    def save_as_mp3(self, text:str, file_name:str = "podcast.mp3"):

        text = text.replace(".", ", ")
        engine.save_to_file(text, file_name)
        engine.runAndWait()

    def save_as_pdf(self, text:str, file_name:str = "Podcast.pdf"):
        text = text.encode('utf-8')

        # using list comprehension
        listToStr = ' '.join([str(elem) for elem in text])

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=listToStr, ln=1, align='C')
        pdf.output(file_name)

