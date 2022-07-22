"""
A module for working with two-dimensional planes.
"""

# internal
from svgen.cartesian.point import DEFAULT, NamedPoints, Point, PointManager


class Plane(PointManager):
    """A class for managing geometric entities."""

    def __init__(
        self, origin: Point = DEFAULT, points: NamedPoints = None
    ) -> None:
        """Initialize this plane."""

        super().__init__(points)
        self.add_point("origin", origin)

    @property
    def origin(self) -> Point:
        """Get the origin of this plane."""
        return self.get_point("origin")
