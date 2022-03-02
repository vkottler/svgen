"""
svgen - A module for the 'circle' element.
"""

# built-in
from typing import List

# internal
from svgen.attribute import Attribute
from svgen.attribute.viewbox import ViewBox
from svgen.cartesian import UNITY, Point, Translation, to_center
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

    def translate(self, move: Translation) -> "Circle":
        """Move this circle by a given translation."""
        return Circle(self.raw.translate(move))

    def scale(self, scale: float = UNITY) -> "Circle":
        """Scale this circle's radius."""
        return Circle(self.raw.scale(scale))

    @property
    def radius(self) -> float:
        """Get this circle's radius."""
        return self.raw.radius

    @property
    def center(self) -> Point:
        """Get this circle's center."""
        return self.raw.center

    def __eq__(self, other: object) -> bool:
        """Determine if this circle is equivalent to another."""

        if not isinstance(other, Circle):
            return NotImplemented
        return self.raw == other.raw


def centered(box: ViewBox, radius_scale: float = UNITY) -> Circle:
    """
    From a viewBox, create a circle that is centered with an appropriately
    scaled radius.
    """

    radius = float(min(box.data.width, box.data.height)) / 2.0
    return Circle(
        CartCircle(radius, to_center(box.center)).scale(radius_scale)
    )
