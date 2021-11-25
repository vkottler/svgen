# =====================================
# generator=datazen
# version=1.9.4
# hash=bbb256bf54dfa67a8f25ae69c9c056d9
# =====================================

"""
svgen - This package's command-line entry-point (boilerplate).
"""

# built-in
import argparse
import logging
import os
import sys
from typing import List

# internal
from svgen import DESCRIPTION, VERSION
from svgen.app import add_app_args, entry


def main(argv: List[str] = None) -> int:
    """Program entry-point."""

    result = 0

    # fall back on command-line arguments
    command_args = sys.argv
    if argv is not None:
        command_args = argv

    # initialize argument parsing
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="set to increase logging verbosity",
    )
    parser.add_argument(
        "-C",
        "--dir",
        default=os.getcwd(),
        dest="dir",
        help="execute from a specific directory",
    )
    starting_dir = os.getcwd()

    add_app_args(parser)

    # parse arguments and execute the requested command
    try:
        args = parser.parse_args(command_args[1:])
        args.version = VERSION
        args.dir = os.path.abspath(args.dir)

        # initialize logging
        log_level = logging.DEBUG if args.verbose else logging.INFO
        logging.basicConfig(
            level=log_level,
            format="%(name)-36s - %(levelname)-6s - %(message)s",
        )

        # change to the specified directory
        os.chdir(args.dir)

        # run the application
        result = entry(args)
    except SystemExit as exc:
        result = 1
        if exc.code is not None:
            result = exc.code

    # return to starting dir
    os.chdir(starting_dir)

    return result
