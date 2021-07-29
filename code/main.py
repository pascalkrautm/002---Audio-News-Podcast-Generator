from mp3converter import Converter
from podcast_generator import PodcastGenerator
from helper import Helper
import ssl
import pickle
from art import *

print(text2art('''Podcast Gen''', font="small"))  # Multi-line print
print("by Krautmacher - Ünal - Meinhold ")
print("With this podcast generator you get an overview of the news that are interesting for you. "
      "You can either have them read to you immediately or download them for later as mp3 or pdf. ")
print(" ")
ssl._create_default_https_context = ssl._create_unverified_context


def main():
    generator = PodcastGenerator()
    keywords = Helper.get_keyword()
    number_of_podcast = generator.generate_podcast(keywords)
    if number_of_podcast > 0:
        read_or_save = Helper.ask_read_or_save()
        while True:
            if read_or_save == "r":
                ask_parameters = Helper.ask_parameters()
                if ask_parameters == "n":
                    voice_rate = Helper.get_voice_rate()
                    voice_volume = Helper.get_voice_volume()
                    voice_language = Helper.get_voice_language()
                    ask_to_save_parameters = Helper.ask_to_save_parameter()
                    if ask_to_save_parameters == "y":
                        # create a list with our default parameters
                        save_parameters = [voice_rate, voice_volume, voice_language]
                        # save our list for next session
                        open_file = open("parameters.pkl", "wb")
                        pickle.dump(save_parameters, open_file)
                        open_file.close()
                    else:
                        pass
                    mp3_converter = Converter(rate=voice_rate, volume=voice_volume, language=voice_language)
                else:
                    # load saved parameters from last session
                    open_file = open("parameters.pkl", "rb")
                    parameter_list = pickle.load(open_file)
                    open_file.close()
                    voice_rate_default = parameter_list[0]
                    voice_volume_default = parameter_list[1]
                    voice_language_default = parameter_list[2]
                    # work with saved parameters
                    mp3_converter = Converter(rate=voice_rate_default, volume=voice_volume_default,
                                              language=voice_language_default)
                mp3_converter.speak(generator.text)
                print("Thank you for using the Podcast Generator. We hope to see you soon!")
                break

            if read_or_save == "m":
                ask_parameters = Helper.ask_parameters()
                if ask_parameters == "n":
                    voice_rate = Helper.get_voice_rate()
                    voice_volume = Helper.get_voice_volume()
                    voice_language = Helper.get_voice_language()
                    ask_to_save_parameters = Helper.ask_to_save_parameter()
                    if ask_to_save_parameters == "y":
                        # create a list with our default parameters
                        save_parameters = [voice_rate, voice_volume, voice_language]
                        # save our list for next session
                        open_file = open("parameters.pkl", "wb")
                        pickle.dump(save_parameters, open_file)
                        open_file.close()
                    else:
                        pass
                    mp3_converter = Converter(rate=voice_rate, volume=voice_volume, language=voice_language)
                else:
                    # load saved parameters from last session
                    open_file = open("parameters.pkl", "rb")
                    parameter_list = pickle.load(open_file)
                    open_file.close()
                    voice_rate_default = parameter_list[0]
                    voice_volume_default = parameter_list[1]
                    voice_language_default = parameter_list[2]
                    # work with saved parameters
                    mp3_converter = Converter(rate=voice_rate_default, volume=voice_volume_default,
                                              language=voice_language_default)
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

        # read_or_save = Helper.ask_read_or_save()
        # if read_or_save == "r":
            # print(generator.text)
            # mp3_converter.speak(generator.text)

        # if read_or_save == "m":
            # mp3_file_name = Helper.ask_name_mp3()
            # mp3_converter.save_as_mp3(generator.text, f"{mp3_file_name}.mp3")

        # if read_or_save == "p":
            # pdf_file_name = Helper.ask_name_pdf()
            # mp3_converter.save_as_pdf(generator.text, f"{pdf_file_name}.pdf")

        # else:
            # mp3_converter.speak(generator.text)

    else:
        print(f"No podcast with Keyword {keywords} found.")


if __name__ == "__main__":
    main()
