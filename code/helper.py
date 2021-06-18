class Helper:
    def __init__(self):
        '''The helper class is initialized'''

    def print_help(self):
        '''Returns the help description'''
        print('helper description')

    @staticmethod
    def get_keyword():
        return input("What topic are you interested in? Just type 'keyword' ('Corona', 'Fußball')")

    @staticmethod
    def get_voice_rate():
        return input("Please select a voice rate between 100 and 200 (Recommendation = 150).")

    @staticmethod
    def get_voice_volume():
        return input("Please select the volume between 0 and 1.0 (Recommendation = 1.0).")

    @staticmethod
    def get_voice_language():
        return input("Please select the language (Type 'german' or 'english').")

help(Helper)
help(Helper.print_help)