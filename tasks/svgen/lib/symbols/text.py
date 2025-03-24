"""
A module that puts text in the symbol area.
"""

# built-in
from typing import Any, List

# internal
from svgen.cartesian.rectangle import Rectangle
from svgen.element import Element


class Text(Element):
    """A text element."""


def add_symbol(box: Rectangle, symbol_config: dict[str, Any]) -> List[Element]:
    """Add the 'vdoer' symbol to a rectangle."""

    result: List[Element] = []

    lines = symbol_config.get("lines", [])

    assert box.square
    padding = box.width / 6
    spacing = box.height / (len(lines) + 2)

    # Get the initial line location.
    loc = box.location.translate(padding, padding + (spacing * 5 / 6))

    style = {
        "font-size": symbol_config.get("size", "5em"),
        "font-family": "monospace",
    }

    for line in lines:
        elem = Text(text=line, attrib=[loc.x_attr, loc.y_attr])
        elem.style.add(style)
        elem.style.add_color(symbol_config.get("color", "white"))
        result.append(elem)

        # Update the location for the next line.
        loc = loc.translate(0, spacing)

    return result
