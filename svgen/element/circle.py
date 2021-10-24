"""
svgen - A module for the 'circle' element.
"""

# built-in
from typing import List

# internal
from svgen.attribute import Attribute
from svgen.cartesian.circle import Circle as CartCircle
from svgen.element import Element


class Circle(Element):
    """A class for circle elements."""

    def __init__(self, circle: CartCircle) -> None:
        """Construct a new circle element."""

        self.raw = circle
        assert self.raw.center.center

        attrs: List[Attribute] = []
        attrs.append(self.raw.radius_attr)
        attrs += [*self.raw.center_attrs]

        super().__init__(attributes=attrs)
