"""
svgen - A module for Cartesian-coordinate interfaces.
"""

# built-in
from math import cos, degrees, isclose, radians, sin, sqrt
from typing import NamedTuple, Union

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


class Angle(NamedTuple):
    """A definition of angle attributes."""

    degrees: float
    radians: float
    sin: float
    cos: float

    @staticmethod
    def from_degrees(val: float) -> "Angle":
        """Create an angle from a degree value."""
        return Angle.from_radians(radians(val))

    @staticmethod
    def from_radians(val: float) -> "Angle":
        """Create an angle from a radian value."""
        return Angle(degrees(val), val, sin(val), cos(val))


ANGLES = {
    "quarter": Angle.from_degrees(90),
    "half": Angle.from_degrees(180),
    "three_quarter": Angle.from_degrees(270),
}


class Translation(NamedTuple):
    """A definition of a translation in a Cartesian coordinate system."""

    dx: float = 0.0
    dy: float = 0.0

    def __eq__(self, other) -> bool:
        """Test if two translations are equivalent."""
        return isclose(self.dx, other.dx, abs_tol=1e-12) and isclose(
            self.dy, other.dy, abs_tol=1e-12
        )

    def rotate(self, angle: Angle = ANGLES["quarter"]) -> "Translation":
        """Rotate this translation vector by some angle."""
        return Translation(
            self.dx * angle.cos - self.dy * angle.sin,
            self.dx * angle.sin + self.dy * angle.cos,
        )


# Common translations.
UP = Translation(0.0, -1.0)
DOWN = Translation(0.0, 1.0)
LEFT = Translation(-1.0, 0.0)
RIGHT = Translation(1.0, 0.0)
VECTORS = {"up": UP, "down": DOWN, "left": LEFT, "right": RIGHT}


class Point(NamedTuple):
    """A definition of a point in a Cartesian coordinate system."""

    x: float = 0.0
    y: float = 0.0
    center: bool = False
    idx: int = -1

    def translate(self, move: Union[Translation, float], *args) -> "Point":
        """Move a point by a given translation."""
        move = (
            Translation(move, *args)
            if not isinstance(move, Translation)
            else move
        )
        return Point(self.x + move.dx, self.y + move.dy, self.center, self.idx)

    def with_index(self, idx: int) -> "Point":
        """Get a new point with the specified index, from an existing point."""
        return Point(self.x, self.y, False, idx)

    @property
    def x_attr(self) -> SimpleAttribute:
        """Get the 'x' attribute for this point."""

        attr = "x"
        if self.center:
            attr = "c" + attr
        elif self.idx >= 0:
            attr += str(self.idx)
        return SimpleAttribute(attr, str(self.x))

    @property
    def y_attr(self) -> SimpleAttribute:
        """Get the 'y' attribute for this point."""

        attr = "y"
        if self.center:
            attr = "c" + attr
        elif self.idx >= 0:
            attr += str(self.idx)
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

    def to_center(self) -> "Point":
        """
        Convert an existing point to one that is definitely a 'center' type.
        """
        return Point(self.x, self.y, True)


def to_center(point: Point) -> Point:
    """Convert an existing point to one that is definitely a 'center' type."""
    return point.to_center()


DEFAULT = Point()
DEFAULT_CENTER = to_center(DEFAULT)
UNITY: float = 1.0


def distance(point_a: Point, point_b: Point = DEFAULT) -> float:
    """Compute the distance between two points."""

    return point_a.distance(point_b)
