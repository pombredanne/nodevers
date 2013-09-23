"""This module includes all the function that
modify (make bolder, change color) the output
printed to the terminal.
"""

__all__ = ["color"]

_foreground_colors = {
    "black" : "\033[30m",
    "red" : "\033[31m",
    "green" : "\033[32m",
    "yellow" : "\033[33m",
    "blue" : "\033[34m",
    "magenta" : "\033[35m",
    "cyan" : "\033[36m",
    "white" : "\033[37m"
}

_background_colors = {
    "black" : "\033[40m",
    "red" : "\033[41m",
    "green" : "\033[42m",
    "yellow" : "\033[43m",
    "blue" : "\033[44m",
    "magenta" : "\033[45m",
    "cyan" : "\033[46m",
    "white" : "\033[47m"
}


def color(string, color=None, effects=[], foreground=True):
    if foreground:
        colors = _foreground_colors
    else:
        colors = _background_colors
    if color in colors:
        string = "%s%s\033[0m" % (colors[color], string)
    for eff in effects:
        func = "_effect_%s" % eff
        if func in globals():
            string = globals()[func](string)
    return string


def _effect_bold(string):
    return "\033[1m%s\033[0m" % string


def _effect_underscore(string):
    return "\033[4m%s\033[0m" % string


def _effect_reverse(string):
    return "\033[7m%s\033[0m" % string
