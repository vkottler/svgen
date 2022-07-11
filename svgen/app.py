"""
svgen - This package's command-line entry-point application.
"""

# built-in
import argparse
from pathlib import Path
from sys import path
from typing import Iterable, cast

# third-party
from vcorelib.dict.config import Config

# internal
from svgen import PKG_NAME
from svgen.attribute.viewbox import ViewBox
from svgen.element.svg import Svg, add_background_grid
from svgen.script import invoke_script


def generate(
    config: Config,
    output: Path,
    cwd: Path,
    scripts: Iterable[Path],
) -> None:
    """Generate a single SVG document."""

    # Add the specified directory to the import path, so external scripts
    # can load their own dependencies.
    cwd_str = str(cwd)
    if cwd_str not in path:
        path.append(cwd_str)

    doc = Svg(ViewBox.from_dict(cast(dict, config)))
    add_background_grid(doc, config["background"], config["grid"])

    # Compose the document, via the external script.
    for script in list(scripts) + [Path(x) for x in config["scripts"]]:
        invoke_script(script, doc, config)

    # Write the composed document to the output file.
    with output.open("w", encoding="utf-8") as output_fd:
        doc.encode(output_fd)

    print(f"Generated '{output}'.")


def initialize_config(
    config: Config, default_height: int, default_width: int
) -> None:
    """Set initial values for SVG document configurations."""

    config.set_if_not("height", default_height)
    config.set_if_not("width", default_width)
    config.set_if_not("scripts", [])
    config.set_if_not("grid", {})
    config.set_if_not("background", {})


def entry(args: argparse.Namespace) -> int:
    """Execute the requested task."""

    try:
        config = Config.from_path(args.config)
    except AssertionError:
        config = Config()

    initialize_config(config, args.height, args.width)

    # Save the initial configuration data.
    original = config.data.copy()

    scripts = set(x.resolve() for x in args.scripts)

    # Generate the main document.
    generate(config, args.output, args.dir, scripts)

    # Generate any document variants.
    for idx, variant in enumerate(config.get("variants", [])):
        # Load the variant's data.
        config = Config(original.copy())
        config.update(variant.get("data", {}))
        initialize_config(config, args.height, args.width)

        # Set the output name for this variant.
        name = args.output.with_suffix("").name
        output = args.output.with_name(
            f"{name}-{variant.get('name', idx)}.svg"
        )

        generate(
            config,
            output,
            args.dir,
            scripts
            | set(Path(x).resolve() for x in variant.get("scripts", [])),
        )

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
