"""
sample - A test script for composing an SVG document.
"""

# internal
from svgen.element.svg import Svg


def compose(svg: Svg, config: dict) -> None:
    """An example function for composing a document."""

    print(svg)
    print(config)
