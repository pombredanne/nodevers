from nodevers.misc import do_nothing


def setup_subparser(subparser):
    parser = subparser.add_parser("clean")
    parser.add_argument(
        "target",
        choices=["tmp", "patches"])
    parser.set_defaults(func=do_nothing)
