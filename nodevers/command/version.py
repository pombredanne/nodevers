from nodevers.misc import do_nothing


def setup_subparser(subparser):
    parser = subparser.add_parser(
        "version",
        help="show the current Node version")
    parser.set_defaults(func=do_nothing)
