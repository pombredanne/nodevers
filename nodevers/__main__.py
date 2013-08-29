"""
This checks if nodevers prefix exists
and then calls cli.parse().
"""
import sys

from . import misc
from . import cli

def main(argv):
    cli.parse(argv[1:])

if __name__ == "__main__":
    main(sys.argv)
