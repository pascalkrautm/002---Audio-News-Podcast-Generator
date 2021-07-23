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
        import textwrap
        from fpdf import FPDF

        text = text.replace("'", "").replace("–", " ").replace("[", "").replace("]", "").replace("’", "")\
            .replace("'", "")
        text.encode("utf-8")

        a4_width_mm = 210
        pt_to_mm = 0.35
        fontsize_pt = 10
        fontsize_mm = fontsize_pt * pt_to_mm
        margin_bottom_mm = 10
        character_width_mm = 7 * pt_to_mm
        width_text = a4_width_mm / character_width_mm

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_auto_page_break(True, margin=margin_bottom_mm)
        pdf.add_page()
        pdf.set_font(family='Arial', size=fontsize_pt)
        splitted = text.split('\n')

        for line in splitted:
            lines = textwrap.wrap(line, width_text)

            if len(lines) == 0:
                pdf.ln()

            for wrap in lines:
                pdf.cell(0, fontsize_mm, wrap, ln=1)

            pdf.output(file_name, 'F')
            print(text)

