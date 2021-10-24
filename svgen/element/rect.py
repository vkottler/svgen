"""
svgen - A module for the 'rect' element.
"""

# built-in
from typing import List

# internal
from svgen.attribute import Attribute, SimpleAttribute
from svgen.cartesian.rectangle import Rectangle
from svgen.element import Element


class Rect(Element):
    """A class for rect elements."""

    def __init__(
        self,
        rect: Rectangle,
        radius_x: float = float(),
        raxius_y: float = float(),
    ) -> None:
        """Construct a new rect element."""

        self.location = rect.location
        self.dimensions = rect.dimensions

        attrs: List[Attribute] = []
        attrs += [*self.location.attrs]
        attrs += [*self.dimensions.attrs]

        if radius_x != float():
            attrs.append(SimpleAttribute("rx", str(radius_x)))
        if raxius_y != float():
            attrs.append(SimpleAttribute("ry", str(raxius_y)))

        super().__init__(attributes=attrs)
