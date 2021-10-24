"""
svgen - A module for interacting with circular entities.
"""

# built-in
from typing import NamedTuple

# internal
from svgen.attribute import SimpleAttribute
from svgen.cartesian import DEFAULT_CENTER, Point, PointAttrs


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
