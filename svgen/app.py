"""
svgen - This package's command-line entry-point application.
"""

# built-in
import argparse

# internal
from svgen.color import Color


def entry(_: argparse.Namespace) -> int:
    """Execute the requested task."""

    themes = []
    """
    blue_gray = [
        (50, "#eceff1"),
        (100, "#cfd8dc"),
        (200, "#b0bec5"),
        (300, "#90a4ae"),
        (400, "#78909c"),
        (500, "#607d8b"),
        (600, "#546e7a"),
        (700, "#455a64"),
        (800, "#37474f"),
        (900, "#263238"),
    ]
    gray = [
        (50, "#f5f5f5"),
        (100, "#e9e9e9"),
        (200, "#d9d9d9"),
        (300, "#c4c4c4"),
        (400, "#9d9d9d"),
        (500, "#7b7b7b"),
        (600, "#555555"),
        (700, "#434343"),
        (800, "#262626"),
        (900, "#000000"),
    ]
    """

    # themes.append(blue_gray)
    # themes.append(gray)

    themes.append([(1, "#e06069"), (1, "#aa2e3f"), (1, "#750019")])
    themes.append([(1, "#ff5a36"), (1, "#ff0000"), (1, "#c20000")])

    for colors in themes:
        sats = []
        for weight, hex_color in colors:
            color = Color.from_hex(hex_color)
            print(f"{color.hsl}\t{color.rgb}")
            sats.append(float(weight) * float(color.hsl.lightness))

        curr = 0.0
        for sat in reversed(sats):
            delta = sat - curr
            curr = sat
            print(delta)

    return 0


def add_app_args(_: argparse.ArgumentParser) -> None:
    """Add application-specific arguments to the command-line parser."""
