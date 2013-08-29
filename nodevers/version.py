"""
This is the module for the version command.
"""

__helpstr__ = """
Usage: nodevers version [-h]

  Summary:
      Print the currently active version

  Options:
      -h    Print this text

"""

import re
import subprocess

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
