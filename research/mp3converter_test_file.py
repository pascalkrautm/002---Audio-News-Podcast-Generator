import pyttsx3
import textwrap
import pickle
from fpdf import FPDF
from helper import Helper

engine = pyttsx3.init()


class Converter(object):  # Create class for the Object "Converter"
    def __init__(self, rate: int = 150, volume: int = 100, language: str = "e", gender: str = "m"):
        self.text = ""
        self.voice_rate = rate
        self.voice_volume = volume
        self.voice_language = language
        self.voice_gender = gender

        # engine.setProperty('rate', self.voice_rate)

        # engine.setProperty('volume', self.voice_volume)

    def voice_language(self):
        if self.voice_language == "e":
            while True:
                self.voice_gender = Helper.get_voice_gender()
                if self.voice_gender == "m":
                    engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
                    break
                if self.voice_gender == "f":
                    engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
                    break
                else:
                    print(r"Your answer may not comply, please note that you may only press 'm' or 'f'.")
        if self.voice_language == "g":
            engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")

    def ask_for_parameters(self, voice_rate, voice_volume, voice_language, ask_to_save_parameters):
        ask_parameters = Helper.ask_parameters()
        while True:
            if ask_parameters == "n":
                self.voice_rate = Helper.get_voice_rate()
                self.voice_volume = Helper.get_voice_volume()
                self.voice_language = Helper.get_voice_language()
                self.ask_to_save_parameters = Helper.ask_to_save_parameter()
                while True:
                    if ask_to_save_parameters == "y":
                        # create a list with our default parameters
                        save_parameters = [voice_rate, voice_volume, voice_language]
                        # save our list for next session
                        open_file = open("parameters.pkl", "wb")
                        pickle.dump(save_parameters, open_file)
                        open_file.close()
                    if ask_to_save_parameters == "n":
                        pass
                    else:
                        print(r"Your answer may not comply, please note that you may only press 'y' or 'n'.")
            if ask_parameters == "y":
                # load saved parameters from last session
                open_file = open("parameters.pkl", "rb")
                parameter_list = pickle.load(open_file)
                open_file.close()
                voice_rate_default = parameter_list[0]
                voice_volume_default = parameter_list[1]
                voice_language_default = parameter_list[2]
                # work with saved parameters
            else:
                print(r"Your answer may not comply, please note that you may only press 'y' or 'n'.")

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
        splitted = text.split('\n')

        for line in splitted:
            lines = textwrap.wrap(line, 75)

            if len(lines) == 0:
                pdf.ln()

            for wrap in lines:
                pdf.cell(0, 3.5, wrap, ln=1)

            pdf.output(file_name, 'F')
            print(text)
