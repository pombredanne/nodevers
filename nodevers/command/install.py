from argparse import REMAINDER
from nodevers.misc import do_nothing


def setup_subparser(subparser):
    parser = subparser.add_parser(
        "install",
        help="install a Node version")
    parser.add_argument(
        "-l", "--list",
        action="store_true",
        default=False,
        help="list all Node versions available for installation")
    parser.add_argument(
        "-b", "--buildargs",
        nargs=REMAINDER,
        help="pass arguments to Node's configure script")
    parser.add_argument(
        "version",
        help="the version to install")
    parser.set_defaults(func=do_nothing)
