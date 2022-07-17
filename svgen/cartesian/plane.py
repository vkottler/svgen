"""
A module for working with two-dimensional planes.
"""

# built-in
from typing import Iterable, NamedTuple, Union

# internal
from svgen.cartesian.mutate import Translation
from svgen.cartesian.point import DEFAULT, NamedPoints, Point, PointManager
from svgen.cartesian.rectangle import Rectangle


class RectangleGrid(NamedTuple):
    """A class for locating points within a rectangle."""

    rect: Rectangle
    columns: int
    rows: int

    @property
    def x_scale(self) -> float:
        """Get the scalar value for 'x' coordinates."""
        return self.rect.width / float(self.columns)

    @property
    def y_scale(self) -> float:
        """Get the scalar value for 'y' coordinates."""
        return self.rect.height / float(self.rows)

    def __call__(self, x: float, y: float) -> Point:
        """Get the true location of a point within this grid."""

        # Ensure the coordinates are within the sub-divisions.
        assert x < self.columns
        assert y < self.rows
        return self.rect.origin.translate(x * self.x_scale, y * self.y_scale)

    @property
    def points(self) -> Iterable[Point]:
        """Iterate over points in the grid."""
        for row in range(self.rows):
            for col in range(self.columns):
                yield self(col, row)

    def box(self, x: float, y: float) -> Rectangle:
        """Get a rectangle object from provided coordinates."""
        return Rectangle.create(self.x_scale, self.y_scale, self(x, y))

    @property
    def boxes(self) -> Iterable[Rectangle]:
        """Iterate over boxes belonging to this grid."""
        for row in range(self.rows):
            for col in range(self.columns):
                yield self.box(col, row)

    def adjust(
        self, columns: int = None, rows: int = None, rect: Rectangle = None
    ) -> "RectangleGrid":
        """Create a new grid from new parameters."""
        if columns is None:
            columns = self.columns
        if rows is None:
            rows = self.rows
        if rect is None:
            rect = self.rect
        return RectangleGrid(rect, columns, rows)

    def translate(
        self, dx: Union[Translation, float], *args, **kwargs
    ) -> "RectangleGrid":
        """Translate this rectangle grid."""

        return RectangleGrid(
            self.rect.translate(dx, *args, **kwargs), self.columns, self.rows
        )


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
