from nodevers.misc import do_nothing


def setup_subparser(subparser):
    parser = subparser.add_parser(
        "use",
        help="set the default Node version")
    parser.add_argument(
        "version",
        help="the version to use as default")
    parser.set_defaults(func=do_nothing)
