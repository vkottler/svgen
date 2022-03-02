"""
svgen - This package's command-line entry-point application.
"""

# built-in
import argparse
from json import load
from pathlib import Path
from typing import cast

# internal
from svgen import PKG_NAME
from svgen.attribute.viewbox import ViewBox
from svgen.config import Config
from svgen.element.svg import Svg
from svgen.script import invoke_script


def entry(args: argparse.Namespace) -> int:
    """Execute the requested task."""

    # Load the top-level configuration.
    try:
        with args.config.open(encoding="utf-8") as config_fd:
            config = Config(load(config_fd))

    # Use a default configuration, if we can't find one,
    except FileNotFoundError:
        config = Config()

    config.set_if_not("height", args.height)
    config.set_if_not("width", args.width)
    config.set_if_not("scripts", [])

    # Compose the document, via the external script.
    doc = Svg(ViewBox.from_dict(cast(dict, config)))
    for script in args.scripts + [Path(x) for x in config["scripts"]]:
        invoke_script(script, doc, config)

    # Write the composed document to the output file.
    with args.output.open("w", encoding="utf-8") as output_fd:
        doc.encode(output_fd)

    return 0


def add_app_args(parser: argparse.ArgumentParser) -> None:
    """Add application-specific arguments to the command-line parser."""

    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        default=Path(f"{PKG_NAME}.json"),
        help="top-level configuration to load (default: '%(default)s')",
    )

    parser.add_argument(
        "--height",
        type=int,
        default=100,
        help=(
            "height of the document, if not specified by "
            "configuration (default: %(default)s)"
        ),
    )

    parser.add_argument(
        "--width",
        type=int,
        default=100,
        help=(
            "width of the document, if not specified by "
            "configuration (default: %(default)s)"
        ),
    )

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(f"{PKG_NAME}.svg"),
        help="file to write SVG output (default: '%(default)s')",
    )

    parser.add_argument(
        "scripts",
        type=Path,
        nargs="*",
        help="scripts to run for composing the SVG document (in order)",
    )
