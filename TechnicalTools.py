"""
/Users/song/PycharmProjects/TechnicalTools/TechnicalTools.py
This is the Technical tools python library created for general purpose shit
just so you know I have no idea what half of this means so don't ask
"""

from inspect import currentframe, getframeinfo


def log(logtype, message, var=None):
    """
    like the logging import but actually useful and less ugly
    """
    linenumber = currentframe().f_back.f_lineno
    filename = getframeinfo(currentframe().f_back).filename.split('/')[-1]
    if logtype == 'info':
        print(f'\033[1;34m[{logtype.upper()}] in {filename} at line {linenumber} - {message} |{var}|')
    elif logtype == 'debug':
        print(f'\033[1;35m[{logtype.upper()}] in {filename} at line {linenumber} - {message} |{var}|')
    elif logtype == 'error':
        print(f'\033[0;31m[{logtype.upper()}] in {filename} at line {linenumber} - {message} |{var}|')
    elif logtype == 'critical':
        print(f'\033[1;31m[{logtype.upper()}] in {filename} at line {linenumber} - {message} |{var}|')


class TextFile:
    """Simple class to format text files"""

    def __init__(self):
        pass

    def __repr__(self):
        return ''

    @staticmethod
    def delnewline(filename, char_amount):
        """Deletes a set number of characters after a new line"""
        finishedtext = ''
        for line in open(filename, 'r'):
            finishedtext += line[char_amount:]
        filename_new = filename.split('.')[0] + '_new.txt'
        try:
            open(filename_new, 'x').write(finishedtext)
        except FileExistsError:
            log('error', 'Created file already exists', filename_new)


def main():
    TextFile.delnewline('words.txt', 4)
    log('debug', 'not critical just epic')


if __name__ == '__main__':
    main()
