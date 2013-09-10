import sys

from argparse import ArgumentParser

from nodevers import __version__
from nodevers.command import setup_subparsers


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="nodevers %s" % __version__,
        help="display the nodevers version")
    subparser = parser.add_subparsers(title="Commands", metavar="<command>")
    setup_subparsers(subparser)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    args = parser.parse_args()
    args.func(args)
