"""
This module connects everything together.
It calls the correct command based on the arguments passed to its
parse() function.
"""

import sys

def help_func(help_str):
    """
    Prints help_str and then
    exits.
    """
    # More Python 2.5/3.x portable than print.
    sys.stdout.write(help_str)
    sys.exit(0)
