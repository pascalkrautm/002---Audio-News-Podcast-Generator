import pyttsx3

engine = pyttsx3.init()

class Converter(object): #Create class for the Object "Converter"
    def __init__(self, file_name : str, text: str, rate, volume, voices):
        self.file_name = file_name
        self.text = text
        self.rate = rate
        self.volume = volume
        self. voices = voices

    def rate_option(self):
        engine_rate = input("Set the rate: (Type: from 100 to 200)")
        engine.setProperty('rate', engine_rate)

    def volume_option(self):
        engine_volume = input("set the volume: (Type: from 0 to 1.0")
        engine.setProperty('volume', engine_volume)

    def voice_option(self):
        engine_voice = input("Which language do you want? (Type: english or german)")
        if engine_voice == "english":
            voice_gender = input("Do you want a male or a female voice? (Type: male or female)")
            if voice_gender == "male":
                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
            else:
                engine.setProperty('voice', "com.apple.speech.synthesis.voice.Victoria")
        else:
            engine.setProperty('voice', "com.apple.speech.synthesis.voice.anna.premium")

    def speak(self):
        with open("test2.txt") as file:
            file = file.read()
        engine.say(file)

    def saving_mp3(self):
        with open("test2.txt") as file:
            file = file.read()
        engine.save_to_file(file, 'test.mp3')
        engine.runAndWait()