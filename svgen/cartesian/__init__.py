"""
svgen - A module for Cartesian-coordinate interfaces.
"""

# built-in
from math import isclose, sqrt
from typing import NamedTuple

# internal
from svgen.attribute import SimpleAttribute


class PointAttrs(NamedTuple):
    """A grouping for 'x' and 'y' attributes."""

    x: SimpleAttribute
    y: SimpleAttribute

    @property
    def x_val(self) -> float:
        """Get the 'x' coordinate for these attributes."""

        return float(self.x.value)

    @property
    def y_val(self) -> float:
        """Get the 'y' coordinate for these attributes."""

        return float(self.y.value)


class Translation(NamedTuple):
    """A definition of a translation in a Cartesian coordinate system."""

    dx: float = float()
    dy: float = float()


class Point(NamedTuple):
    """A definition of a point in a Cartesian coordinate system."""

    x: float = float()
    y: float = float()
    center: bool = False

    def translate(self, move: Translation) -> "Point":
        """Move a point by a given translation."""

        return Point(self.x + move.dx, self.y + move.dy, self.center)

    @property
    def x_attr(self) -> SimpleAttribute:
        """Get the 'x' attribute for this point."""

        attr = "x"
        if self.center:
            attr = "c" + attr
        return SimpleAttribute(attr, str(self.x))

    @property
    def y_attr(self) -> SimpleAttribute:
        """Get the 'y' attribute for this point."""

        attr = "y"
        if self.center:
            attr = "c" + attr
        return SimpleAttribute(attr, str(self.y))

    @property
    def attrs(self) -> PointAttrs:
        """Get the 'x' and 'y' attributes for this point."""

        return PointAttrs(self.x_attr, self.y_attr)

    def __eq__(self, other: object) -> bool:
        """Determine if two points are the same."""

        if not isinstance(other, Point):
            return NotImplemented
        return isclose(self.x, other.x) and isclose(self.y, other.y)

    def distance(self, point: "Point") -> float:
        """Compute the distance from this point to another."""

        run = point.x - self.x
        rise = point.y - self.y
        return sqrt(run * run + rise * rise)


def to_center(point: Point) -> Point:
    """Convert an existing point to one that is definitely a 'center' type."""

    return Point(point.x, point.y, True)


DEFAULT = Point()
DEFAULT_CENTER = to_center(DEFAULT)
UNITY: float = 1.0


def distance(point_a: Point, point_b: Point = DEFAULT) -> float:
    """Compute the distance between two points."""

    return point_a.distance(point_b)
