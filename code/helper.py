class Helper:
    def __init__(self):
        """The helper class is initialized"""

    @staticmethod
    def print_help():
        """Returns the help description"""
        helper_description = ("",
                              "To generate the RSS feed, you need to answer several questions."
                              "Below are these questions with their purpose for clarification and understanding:",
                              "-In the first step you need to enter your desired topics so that the present program"
                              " can search the Internet according to your entered interests.",
                              "-You will then be asked whether you want the news to be generated as a pdf, MP3 or"
                              " voice-speak. If you choose the pdf or MP3 variant, please note that the result will"
                              " be saved in the 'data' folder. If you decide for PDF, there is nothing more to do, "
                              "accept entering the name you wish for you file. ",
                              "-If you use the MP3 or voice-speak variant there are further questions to consider"
                              " You have to set the voice rate, language and volume for your output. "
                              " You will be asked if you want to use the default settings. "
                              " Note: When you start the program for the first time, please note to enter your "
                              "desired parameters. Otherwise the program will start with the default parameters "
                              "set by us. You can change the parameters at any time according to your preferences.",
                              "")
        for value in helper_description:
            print(value)

    @staticmethod
    def get_keyword():
        keyword = str(input("To start enter one or more comma separated topics (eg: corona, soccer, germany) or enter "
                            "'h' to get an introduction into the program"))
        if keyword == "h":
            Helper.print_help()
            keyword = str(input("To start enter one or more comma separated topics (eg: corona, soccer, germany)"))
            keywords = keyword.lower().split(",")
            print(f"Given topics are {keywords}")
            return keywords
        else:
            keywords = keyword.lower().split(",")
            print(f"Given topics are {keywords}")
            return keywords

    @staticmethod
    def ask_parameters():
        return input(
            "Would you like to use the saved settings (voice rate, language, volume) for the Podcast?"
            "(Type 'y' for yes or 'n' for no.)")

    @staticmethod
    def get_voice_rate():
        return input("Please select a voice rate between 100 and 200 (Recommendation = 150).")

    @staticmethod
    def get_voice_volume():
        return input("Please select the volume between 0 and 1.0 (Recommendation = 1.0).")

    @staticmethod
    def get_voice_language():
        return input("Please select german or english as language (Type 'g' for german or 'e' for english).")

    @staticmethod
    def get_voice_gender():
        return input("Please select the speakers gender (Type 'm' for male or 'f' for female).")

    @staticmethod
    def ask_to_save_parameter():
        return input(
            "Do you like to save the parameter you have entered as new standard parameters for the next time? (y/n)")

    @staticmethod
    def ask_read_or_save():
        return input(
            "Please select whether you want the podcast to be read aloud (r) now, saved as an mp3 (m) for later, "
            "or saved as a pdf (p) for later (r/m/p).")

    @staticmethod
    def ask_name_mp3():
        return input("What name should the mp3-file have? (Please do not type '.mp3' after the name)")

    @staticmethod
    def ask_name_pdf():
        return input("What name should the pdf-file have? (Please do not type '.pdf' after the name)")

# help(Helper)
# help(Helper.print_help)
