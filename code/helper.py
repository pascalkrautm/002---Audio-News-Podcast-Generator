class Helper:
    def __init__(self):
        '''The helper class is initialized'''

    def print_help(self):
        '''Returns the help description'''
        print('helper description')
    @staticmethod
    def get_keyword():
        return input("Keyword?")

help(Helper)
help(Helper.print_help)