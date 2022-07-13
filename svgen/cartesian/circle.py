"""
svgen - A module for interacting with circular entities.
"""

# built-in
from math import isclose
from typing import NamedTuple

# internal
from svgen.attribute import SimpleAttribute
from svgen.cartesian import UNITY
from svgen.cartesian.mutate import Translation
from svgen.cartesian.point import DEFAULT_CENTER, Point, PointAttrs


class CircleAttrs(NamedTuple):
    """A grouping for 'width' and 'center' attributes for a cicle."""

    radius: SimpleAttribute
    center: PointAttrs

    @property
    def radius_val(self) -> float:
        """Get the 'radius' value for this circle."""

        return float(self.radius.value)


class Circle(NamedTuple):
    """A radius and center describing a circle."""

    radius: float
    center: Point = DEFAULT_CENTER

    @property
    def radius_attr(self) -> SimpleAttribute:
        """Get the 'radius' attribute for this circle."""

        return SimpleAttribute("r", str(self.radius))

    @property
    def center_attrs(self) -> PointAttrs:
        """Get the 'center' attributes for this circle."""

        assert self.center.center
        return self.center.attrs

    @property
    def attrs(self) -> CircleAttrs:
        """Get the 'radius' and 'center' attributes for this circle."""

        return CircleAttrs(self.radius_attr, self.center_attrs)

    def translate(self, move: Translation) -> "Circle":
        """Move this circle by a given translation."""

        return Circle(self.radius, self.center.translate(move))

    def scale(self, scale: float = UNITY) -> "Circle":
        """Scale this circle's radius."""

        return Circle(self.radius * scale, self.center)

    def __eq__(self, other: object) -> bool:
        """Determine if this circle is equivalent to another."""

        if not isinstance(other, Circle):
            return NotImplemented
        return (
            isclose(self.radius, other.radius) and self.center == other.center
        )
