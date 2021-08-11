from art import *
from converter import Converter
from helper import Helper
from podcast_generator import PodcastGenerator

print(text2art('''Podcast Gen''', font="small"))  # Multi-line print
print("by Krautmacher - Ünal - Meinhold ")
print("With this podcast generator you get an overview of the news that are interesting for you."
      "You can either have them read to you immediately or download them for later as mp3 or pdf.")
print(" ")


def main():
    while True:
        try:
            generator = PodcastGenerator()
            keywords = Helper.get_keyword()
            number_of_podcast = generator.generate_podcast(keywords)
            if number_of_podcast > 0:
                while True:
                    read_or_save = Helper.ask_read_or_save()
                    if read_or_save == "r":
                        mp3_converter = Converter()
                        mp3_converter.parameter_settings()
                        mp3_converter.speak(generator.text)
                        print("Thank you for using the Podcast Generator. We hope to see you soon!")
                        break
                    if read_or_save == "m":
                        mp3_converter = Converter()
                        mp3_converter.parameter_settings()
                        mp3_file_name = Helper.ask_name_mp3()
                        mp3_converter.save_as_mp3(generator.text, f"{mp3_file_name}.mp3")
                        print("Thank you for using the Podcast Generator. We hope to see you soon!")
                        break
                    if read_or_save == "p":
                        pdf_file_name = Helper.ask_name_pdf()
                        mp3_converter = Converter()
                        mp3_converter.save_as_pdf(generator.text, f"{pdf_file_name}.pdf")
                        print("Thank you for using the Podcast Generator. We hope to see you soon!")
                        break
                    else:
                        print(r"Your answer may not comply, please note that you may only press 'r', 'm' or 'p'.")
            else:
                print(f"No podcast with Keyword {keywords} found. Please rerun the app")
            break
        except AttributeError:
            print("Ups an error has occurred. Please try another keyword.")


if __name__ == "__main__":
    main()
