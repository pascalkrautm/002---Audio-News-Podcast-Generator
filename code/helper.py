class Helper:
    def __init__(self):
        '''The helper class is initialized'''

    def print_help(self):
        '''Returns the help description'''
        print('helper description')

    @staticmethod
    def get_keyword():
        keywords = []
        keyword = input("Type in your first keyword' ('Corona', 'Fußball')")
        keywords.append(keyword)
        answer = input("Do you wish to add a keyword? (y/n)")
        while answer == "y":
            keyword = input("Type in your next keyword!")
            keywords.append(keyword)
            answer = input("Do you wish to add a keyword? (y/n)")
        else:
            pass
        #convert to small letters
        for words in range(len(keywords)):
            keywords[words] = keywords[words].lower()
        return keywords

    @staticmethod
    def ask_parameters():
        return input("Do you want to use the recommended parameters? (y/n)")

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
        return input("Read podcast (r) or save as mp3 (s)? (r/s)")

help(Helper)
help(Helper.print_help)