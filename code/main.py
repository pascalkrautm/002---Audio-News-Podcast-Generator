from mp3converter import Converter
from podcast_generator import PodcastGenerator
from helper import Helper
import ssl
from art import *

print(text2art('''Podcast Gen''', font="small")) # Multi-line print
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    generator = PodcastGenerator()
    keywords = Helper.get_keyword()
    #keyword = input("What topic are you interested in? Just type 'keyword' ('Corona', 'Fußball')")
    number_of_podcast = generator.generate_podcast(keywords)
    if number_of_podcast > 0:
        ask_parameters = Helper.ask_parameters()
        if ask_parameters == "n":
            voice_rate = Helper.get_voice_rate()
            voice_volume = Helper.get_voice_volume()
            voice_language = Helper.get_voice_language()
            ask_to_save_parameters = Helper.ask_to_save_parameter()
            if ask_to_save_parameters == "y":
                # Save parameters for next time.
                pass
            else:
                pass
            mp3_converter = Converter(rate=voice_rate, volume=voice_volume, language=voice_language)
            mp3_converter.speak(generator.text)
        else:
            mp3_converter = Converter(rate=150, volume=1, language="german")
            mp3_converter.speak(generator.text)
    else:
        print(f"No podcast with Keyword {keywords} found.")


if __name__ == "__main__":
    main()

