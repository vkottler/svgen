# =====================================
# generator=datazen
# version=3.0.8
# hash=f2f8adaaa3e69e38b7e265b9e5bb7a5e
# =====================================

"""
This package's command-line entry-point (boilerplate).
"""

# built-in
import argparse
import logging
import os
from pathlib import Path
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
        default=Path.cwd(),
        dest="dir",
        type=Path,
        help="execute from a specific directory",
    )
    starting_dir = Path.cwd()

    add_app_args(parser)

    # parse arguments and execute the requested command
    try:
        args = parser.parse_args(command_args[1:])
        args.version = VERSION
        args.dir = args.dir.resolve()

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
