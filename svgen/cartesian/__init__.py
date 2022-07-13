"""
svgen - A module for Cartesian-coordinate interfaces.
"""

# internal
from svgen.cartesian.point import DEFAULT, Point

UNITY: float = 1.0


def distance(point_a: Point, point_b: Point = DEFAULT) -> float:
    """Compute the distance between two points."""

    return point_a.distance(point_b)
