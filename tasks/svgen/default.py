"""
A sample svgen script.
"""

# built-in
from typing import Any

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.element import Element


def compose(viewbox: ViewBox, config: dict[str, Any]) -> list[Element]:
    """An example function for composing a document."""

    print(viewbox)
    print(config)

    return []
