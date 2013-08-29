"""
This is the module for the versions command.
"""

__helpstr__ = """Usage: nodevers versions [-h]

  Summary:
      Print all the installed versions.

  Options:
      -h    Print this text

"""

import os
import sys
from . import misc
from . import cli

def get_versions_list():
    """
    Return a list of all the installed Node versions.
    """
    versions_dir = misc.get_versions_dir()
    # os.path.isdir() will fail unless we do this.
    os.chdir(versions_dir)
    versions = [ver for ver in os.listdir(versions_dir) if os.path.isdir(ver)]
    return versions

def parse(args):
    """
    Parse the arguments and call the correct functions
    based on them.
    """
    if len(args) == 0:
        for ver in get_versions_list():
            sys.stdout.write("%s\n" % ver)
    elif "-h" in args or "--help" in args:
        cli.help_func(__helpstr__)
    else:
        for i in args:
            sys.stdout.write("Unknown option: %s\n" % i)
            cli.help_func(__helpstr__)
