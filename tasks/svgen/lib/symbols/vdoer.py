"""
A module implementing the 'vdoer' symbol.
"""

# built-in
from typing import Any, List

# internal
from svgen.attribute import PossibleAttributes
from svgen.cartesian.rectangle import Rectangle
from svgen.cartesian.rectangle.grid import RectangleGrid
from svgen.color.resolve import get_color
from svgen.element import Element
from svgen.element.line import Line


def add_symbol(box: Rectangle, symbol_config: dict[str, Any]) -> List[Element]:
    """Add the 'vdoer' symbol to a rectangle."""

    result: List[Element] = []

    if not symbol_config.get("enabled", True):
        return result

    assert box.square

    grid_divisions = 16
    grid = RectangleGrid(box, grid_divisions, grid_divisions)

    line_attrs: PossibleAttributes = {
        "stroke-linecap": "round",
        "style": (
            f"stroke:{get_color(symbol_config.get('color', 'white'))};"
            f"stroke-width:{box.width / 16.0}"
        ),
    }

    midpoint = grid_divisions / 2
    margin = 2
    length = 3

    # Left bracket.
    result.append(
        Line(
            grid(margin, midpoint),
            grid(margin + length, midpoint + length),
            line_attrs,
        )
    )
    result.append(
        Line(
            grid(margin, midpoint),
            grid(margin + length, midpoint - length),
            line_attrs,
        )
    )

    # Right bracket.
    result.append(
        Line(
            grid(grid_divisions - margin, midpoint),
            grid(grid_divisions - margin - length, midpoint + length),
            line_attrs,
        )
    )
    result.append(
        Line(
            grid(grid_divisions - margin, midpoint),
            grid(grid_divisions - margin - length, midpoint - length),
            line_attrs,
        )
    )

    # Middle slash.
    center = box.center
    dx = box.width * float(length / grid_divisions) / 2.0
    dy = box.height * float(length / grid_divisions) * (5.0 / 4.0)
    result.append(
        Line.create(
            center.x,
            center.y,
            center.x - dx,
            center.y + dy,
            line_attrs,
        )
    )
    result.append(
        Line.create(
            center.x,
            center.y,
            center.x + dx,
            center.y - dy,
            line_attrs,
        )
    )

    return result
