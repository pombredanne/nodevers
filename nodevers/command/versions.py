from nodevers.misc import do_nothing


def setup_subparser(subparser):
    parser = subparser.add_parser(
        "versions",
        help="list all the Node versions")
    parser.add_argument(
        "-a", "--all",
        action="store_true",
        default=False,
        help="list all Node versions available")
    parser.set_defaults(func=do_nothing)
