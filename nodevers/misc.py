from __future__ import print_function
import sys

from nodevers.helper import color as c

__all__ = ["warn", "error"]

def warn(message):
    """Output a warning message.

    Keyword arguments:
        message -- the message to be printed
    """
    message = "%s: %s" % (c("warning", "yellow"), message)
    print(message, file=sys.stderr)


def error(message, errno=1):
    """Output an error message and exit.

    Keyword arguments:
        message -- the message to be printed
        errno -- the exit code to be returned
    """
    message = "%s: %s" % (c("error", "red"), message)
    print(message, file=sys.stderr)
    sys.exit(errno)


def do_nothing(*args):
    """Dummy method. Will be removed."""
    pass
