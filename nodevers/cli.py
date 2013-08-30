"""
This module connects everything together.
It calls the correct command based on the arguments passed to its
parse() function.
"""

import sys
import nodevers

__helpstr__ = """nodist %s
Usage: nodist <command> [options]

  Commands:
      install           Install a Node
      use               Make the specified Node version the default
      versions          List all the currently installed versions
      help              Print this
      remove            Uninstall the specified Node version

""" % nodevers.__version__

def help_func(help_str):
    """
    Prints help_str and then
    exits.
    """
    # More Python 2.5/3.x portable than print.
    sys.stdout.write(help_str)
    sys.exit(0)

def parse(args):
    """
    Parse the CLI options and call
    the correct functions based on them.
    """
    known_commands = ("version", "versions", "install", "help",
            "use", "remove")
    if len(args) == 0:
        help_func(__helpstr__)
    elif args[0] == "help" or args[0] == "-h" or args[0] == "--help":
        help_func(__helpstr__)
    elif args[0] == "-v" or args[0] == "--version":
        sys.stdout.write("nodevers %s\n" % nodevers.__version__)
    elif args[0] not in known_commands:
        sys.stderr.write("Error: unrecognized command: '%s'\n" %
                args[0])
        sys.exit(-1)
    if args[0] == "version":
        import nodevers.version as version
        version.parse(args[1:])
    elif args[0] == "versions":
        import nodevers.versions as versions
        versions.parse(args[1:])
    elif args[0] == "install":
        import nodevers.install as install
        install.parse(args[1:])
    elif args[0] == "use":
        import nodevers.use as use
        use.parse(args[1:])
    elif args[0] == "remove":
        import nodevers.remove as remove
        remove.parse(args[1:])
