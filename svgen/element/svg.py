"""
svgen - A module for the 'svg' element.
"""

# built-in
from typing import List

# internal
from svgen.attribute import XMLNS, Attribute
from svgen.attribute.viewbox import ViewBox
from svgen.element import Element


class Svg(Element):
    """A class for svg elements."""

    def __init__(self, viewbox: ViewBox, document: bool = True) -> None:
        """Construct a new svg element (or document)."""

        self.viewbox = viewbox
        attrs: List[Attribute] = [self.viewbox]
        if document:
            attrs.append(XMLNS)
        super().__init__(attributes=attrs)
