import pyttsx3

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
        if engine_voice == "english":
            voice_gender = input("Do you want a male or a female voice? (Type: male or female)")
            if voice_gender == "male":
                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
            else:
                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
        else:
            engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")

    def speak(self, text:str):
        engine.say(text)
        engine.runAndWait()

    def save_as_mp3(self, text:str, file_name:str = "podcast.mp3"):
        engine.save_to_file(text, file_name)
        engine.runAndWait()
