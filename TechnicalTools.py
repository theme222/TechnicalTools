"""
/Users/song/PycharmProjects/TechnicalTools/TechnicalTools.py
This is the Technical tools python library created for general purpose shit
just so you know I have no idea what half of this means so don't ask
"""

import inspect
import logging


# A shorter version of the logging import using inspect to find the actual line number
def log(logtype, message, var=None):
    linenumber = inspect.currentframe().f_back.f_lineno
    logging.basicConfig(level=logging.DEBUG,
                        format=f'[%(levelname)s] in %(filename)s at line {linenumber} - %(message)s |{var}|')
    if logtype == 'Info' or logtype == 'info':
        logging.info(message)
    elif logtype == 'Debug' or logtype == 'debug':
        logging.debug(message)
    elif logtype == 'Error' or logtype == 'error':
        logging.error(message)
    elif logtype == 'Critical' or logtype == 'critical':
        logging.critical(message)


def main():
    log('critical', 'not critical just epic')


if __name__ == '__main__':
    main()
