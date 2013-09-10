commands = [
    "install",
    "remove",
    "use",
    "version",
    "version",
    "patch",
    "clean"
    ]


def setup_subparsers(subparser):
    for cmd in commands:
        try:
            temp = __import__("nodevers.command.%s" % cmd,
                              fromlist=["setup_subparser"])
            setup_subparser = temp.setup_subparser
        except ImportError:
            pass
        setup_subparser(subparser)
