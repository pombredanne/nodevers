from __future__ import print_function
import sys


def warn(message):
    """Print the message to stderr."""
    print(message, file=sys.stderr)


def error(message, errno=1):
    """Print the message to stderr and exit.

    Keyword arguments:
        errno:      the exit code to be returned
    """
    warn(message)
    sys.exit(errno)


def do_nothing(*args):
    """Dummy method. Will be removed."""
    pass
