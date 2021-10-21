"""
svgen - A module for Cartesian-coordinate interfaces.
"""

# built-in
from math import isclose, sqrt
from typing import NamedTuple


class Point(NamedTuple):
    """A definition of a point in a Cartesian coordinate system."""

    x: float = 0.0
    y: float = 0.0

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


def distance(point_a: Point, point_b: Point = Point()) -> float:
    """Compute the distance between two points."""

    return point_a.distance(point_b)
