"""
This is the module for the version command.
"""

__helpstr__ = """Usage: nodevers version [-h]

  Summary:
      Print the currently active version

  Options:
      -h    Print this text

"""

import re
import subprocess
import sys
from . import cli

def current_version():
    """
    Try to get the current version.
    """
    # We'll let parse() handle the exceptions.
    process = subprocess.Popen(["node", "-v"], stdout=subprocess.PIPE)
    node_output = process.stdout.read()
    regex = "v(\d+\.\d+\.\d+)"
    match = re.match(regex, node_output)
    version = match.group(1)
    return version

def parse(args):
    """
    Parse the arguments and call the correct functions
    based on them.
    """
    if len(args) == 0:
        try:
            version = current_version()
            sys.stdout.write("%s\n" % version)
        except OSError:
            sys.stderr.write("There is no currently active Node.")
    elif "-h" in args or "--help" in args:
        cli.help_func(__helpstr__)
    else:
        for i in args:
            sys.stdout.write("Unknown option: %s\n" % i)
            cli.help_func(__helpstr__)
