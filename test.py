"""
sample - A test script for composing an SVG document.
"""

# built-in
from typing import List

# internal
from svgen.attribute.style import Style
from svgen.attribute.viewbox import ViewBox
from svgen.color import Color
from svgen.element import Element
from svgen.element.circle import centered


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    print(config)

    red = Style()
    red.add_color(Color.from_ctor("red"))

    return [centered(viewbox).add_attribute(red)]
