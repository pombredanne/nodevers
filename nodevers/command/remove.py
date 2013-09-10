from nodevers.misc import do_nothing


def setup_subparser(subparser):
    parser = subparser.add_parser(
        "remove",
        help="remove a Node version")
    parser.add_argument(
        "version",
        help="the version to remove")
    parser.set_defaults(func=do_nothing)
