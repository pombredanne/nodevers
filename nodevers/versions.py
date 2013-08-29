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
from . import misc

def get_versions_list():
    """
    Return a list of all the installed Node versions.
    """
    versions_dir = misc.get_versions_dir()
    # os.path.isdir() will fail unless we do this.
    os.chdir(versions_dir)
    versions = [ver for ver in os.listdir(versions_dir) if os.path.isdir(ver)]
    return versions
