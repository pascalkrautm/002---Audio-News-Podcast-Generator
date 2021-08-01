import pyttsx3
import textwrap
import pickle
from fpdf import FPDF
from helper import Helper

engine = pyttsx3.init()


class Converter(object):  # Create class for the Object "Converter"
    def __init__(self, rate: int = 150, volume: int = 100, language: str = "e", gender: str = "m"):
        self.text = ""
        self.rate = rate
        self.volume = volume
        self.language = language
        self.gender = gender

    def parameter_settings(self):
        while True:
            engine_parameters = Helper.ask_parameters()
            if engine_parameters == "n":
                self.rate = Helper.get_voice_rate()
                engine.setProperty('rate', self.rate)
                self.volume = Helper.get_voice_volume()
                engine.setProperty('volume', self.volume)
                while True:
                    self.language = Helper.get_voice_language()
                    if self.language == "e":
                        while True:
                            self.gender = Helper.get_voice_gender()
                            if self.gender == "m":
                                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
                                break
                            if self.gender == "f":
                                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
                                break
                            else:
                                print(r"Your answer may not comply, please note that you may only press 'm' or 'f'")
                        break
                    if self.language == "g":
                        engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")
                        break
                    else:
                        print(r"Your answer may not comply, please note that you may only press 'g' or 'e'")
                while True:
                    engine_save_parameter = Helper.ask_to_save_parameter()
                    if engine_save_parameter == "y":
                        # create a list with our default parameters
                        save_parameters = [self.rate, self.volume, self.language, self.gender]
                        # save our list for next session
                        open_file = open("parameters.pkl", "wb")
                        pickle.dump(save_parameters, open_file)
                        open_file.close()
                        break
                    if engine_save_parameter == "n":
                        pass
                        break
                    else:
                        print(r"Your answer may not comply, please note that you may only press 'y' or 'n'")
                break
            if engine_parameters == "y":
                try:
                    # load saved parameters from last session
                    open_file = open("parameters.pkl", "rb")
                    parameter_list = pickle.load(open_file)
                    open_file.close()
                    voice_rate_default = parameter_list[0]
                    voice_volume_default = parameter_list[1]
                    voice_language_default = parameter_list[2]
                    voice_gender_default = parameter_list[3]
                    engine.setProperty('rate', voice_rate_default)
                    engine.setProperty('volume', voice_volume_default)
                    if voice_language_default == "e":
                        if voice_gender_default == "m":
                            engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
                        if voice_gender_default == "f":
                            engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
                    if self.language == "g":
                        engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")
                except IOError:
                    engine.setProperty('rate', 200)
                    engine.setProperty('volume', 1.0)
                    engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
                break
            else:
                print(r"Your answer may not comply, please note that you may only press 'y' or 'n'")

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
