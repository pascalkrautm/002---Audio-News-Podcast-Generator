import pyttsx3
import textwrap
from fpdf import FPDF
from helper import Helper

engine = pyttsx3.init()


class Converter(object):  # Create class for the Object "Converter"
    def __init__(self, rate: int = 150, volume: int = 100, language: str = "english"):
        self.text = ""
        self.rate = rate
        self.volume = volume
        self.language = language

        engine.setProperty('rate', self.rate)

        engine.setProperty('volume', self.volume)

        engine_voice = self.language
        if engine_voice == "e":
            while True:
                voice_gender = Helper.get_voice_gender()
                if voice_gender == "m":
                    engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
                    break
                if voice_gender == "f":
                    engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
                    break
                else:
                    print(r"Your answer may not comply, please note that you may only press m or f")
        if engine_voice == "g":
            engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")

    def speak(self, text: str):
        engine.say(text)
        engine.runAndWait()

    def save_as_mp3(self, text: str, file_name: str = "podcast.mp3"):
        text = text.replace(".", ", ")
        engine.save_to_file(text, file_name)
        engine.runAndWait()

    def save_as_pdf(self, text: str, file_name: str = "Podcast.pdf"):
        text_encoded = text.encode('latin-1', 'replace').decode('latin-1')
        text = text_encoded.replace("?", ".").replace("[", "").replace("]", "").replace("'", "")

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_auto_page_break(True, margin=10)
        pdf.add_page()
        pdf.set_font(family='Courier', size=12)
        splitter = text.split('\n')

        for line in splitter:
            lines = textwrap.wrap(line, 75)
            if len(lines) == 0:
                pdf.ln()
            for wrap in lines:
                pdf.cell(0, 4, wrap, ln=1)
            pdf.output(file_name, 'F')
