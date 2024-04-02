"""
This is the Technical tools python library created for general purpose stuff
just so you know I have no idea what half of this means so don't ask
"""

from inspect import currentframe, getframeinfo
import os

show_filename = True
show_line_number = True


def log(message, logtitle="info", var=None, color="blue"):
    """
    printing but with color!
    :param message:
    :param var:
    :param logtitle:
    :param var:
    :param color:
    """
    if var is not None:
        var = '|' + str(var) + '|'
    else:
        var = ""

    linenumber = currentframe().f_back.f_lineno
    if os.name == 'nt':
        filename = getframeinfo(currentframe().f_back).filename.split('\\')[-1]
    else:
        filename = getframeinfo(currentframe().f_back).filename.split('/')[-1]

    color_codes = {"black": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34, "purple": 35, "cyan": 36, "white": 37}
    try:
        color = color_codes[color]
    except KeyError:
        log("Color not found", logtitle="error", color="red")
        color = "cyan"

    filenametxt = ""
    linenumbertxt = ""
    if show_filename:
        filenametxt = f"in {filename} "
    if show_line_number:
        linenumbertxt = f"at line {linenumber} "
    print_message = f'\033[1;{color}m[{logtitle.upper()}] {filenametxt}{linenumbertxt}- {message} {var}\033[0m'
    print(print_message)


if __name__ == '__main__':
    log("aaadsffasd")
