class Helper:
    def __init__(self):
        '''The helper class is initialized'''

    def print_help(self):
        '''Returns the help description'''
        print('helper description')

    @staticmethod
    def get_keyword():
        keywords = []
        keyword = str(input("Enter comma separated topics (eg: corona, soccer, germany)"))
        keywords = keyword.lower().split(",")
        print(f"Given topics are {keywords}")

        return keywords

    @staticmethod
    def ask_parameters():
        return input("Do you want to use the recommended parameters for the speaker? (eg. voice rate, language, volume) (y/n)")

    @staticmethod
    def get_voice_rate():
        return input("Please select a voice rate between 100 and 200 (Recommendation = 150).")

    @staticmethod
    def get_voice_volume():
        return input("Please select the volume between 0 and 1.0 (Recommendation = 1.0).")

    @staticmethod
    def get_voice_language():
        return input("Please select the language (Type 'german' or 'english').")

    @staticmethod
    def ask_to_save_parameter():
        return input("Do you want to save the parameter as new standard parameters for the next time? (y/n)")

    @staticmethod
    def ask_read_or_save():
        return input("Read podcast (r) or save as mp3 (m) or save as pdf (p)? (r/m/p)")

help(Helper)
help(Helper.print_help)