import pyttsx3

engine = pyttsx3.init()

en_voice_male_id = "com.apple.speech.synthesis.voice.Alex"
en_voice_female_id = "com.apple.speech.synthesis.voice.Victoria"
us_voice_male_id = "com.apple.speech.synthesis.voice.Fred"
de_voice_female_id = "com.apple.speech.synthesis.voice.anna.premium"
voice = engine.getProperty('voice')

engine_voice = input("Which language do you want? (Type: english or german)")
if engine_voice == "english":
    voice_gender = input("Do you want a male or a female voice? (Type: male or female)")
    if voice_gender == "male":
        engine.setProperty('voice', "com.apple.speech.synthesis.voice.Alex")
    else:
        engine.setProperty('voice', en_voice_female_id)
else:
    engine.setProperty('voice', de_voice_female_id)

voice = engine.getProperty('voice')
engine.setProperty('rate', 150)

with open("podcast.txt") as file:
   file = file.read()

engine.say(file)

engine.runAndWait()
