from nodevers.misc import do_nothing


def setup_subparser(subparser):
    parser = subparser.add_parser(
        "patch",
        help="import or delete patches")
    parser.add_argument(
        "-l", "--list",
        metavar="VERSION",
        nargs="?",
        default="all",
        help="list the patches for the specified version")
    parser.add_argument(
        "-i", "--import",
        metavar=("PATCH", "VERSION"),
        nargs=2,
        help="import the patch for the specified version")
    parser.add_argument(
        "-d", "--delete",
        metavar=("PATCH", "VERSION"),
        nargs=2,
        help="remove the patch for the specified version")
    parser.set_defaults(func=do_nothing)
