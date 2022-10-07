"""
A module for working with corners of rectangles.
"""

# built-in
from enum import Enum
from math import isclose
from typing import NamedTuple

# internal
from svgen.cartesian import Dimensions
from svgen.cartesian.mutate import VECTORS, Translation
from svgen.cartesian.point import Point


class CornerScalar(NamedTuple):
    """A collection of attributes for a rectangle's corner."""

    from_origin: Translation
    vector: Translation

    def __str__(self) -> str:
        """Get a suitable string for this corner scalar."""
        return f"from_origin={self.from_origin}, vector={self.vector}"

    def __hash__(self) -> int:
        """Get a suitable hash for this corner scalar."""
        return hash(str(self))

    def __eq__(self, other) -> bool:
        """Determine if this corner scalar is equivalent to another."""
        return bool(
            self.from_origin == other.from_origin
            and self.vector == other.vector
        )

    @property
    def vertical(self) -> bool:
        """Determine if this vector is vertical."""
        return not isclose(self.vector.dy, 0.0)

    @property
    def horizontal(self) -> bool:
        """Determine if this vector is horizontal."""
        return not isclose(self.vector.dx, 0.0)


class RectangleCorner(Enum):
    """An enumeration of the corners of a rectangle."""

    TOP_LEFT = CornerScalar(Translation(0.0, 0.0), VECTORS["down"])
    TOP_RIGHT = CornerScalar(Translation(1.0, 0.0), VECTORS["left"])
    BOTTOM_LEFT = CornerScalar(Translation(0.0, 1.0), VECTORS["right"])
    BOTTOM_RIGHT = CornerScalar(Translation(1.0, 1.0), VECTORS["up"])

    @property
    def on_top(self) -> bool:
        """Determine if this corner is on the top side."""
        return (
            self is RectangleCorner.TOP_LEFT
            or self is RectangleCorner.TOP_RIGHT
        )

    @property
    def on_bottom(self) -> bool:
        """Determine if this corner is on the bottom side."""
        return (
            self is RectangleCorner.BOTTOM_LEFT
            or self is RectangleCorner.BOTTOM_RIGHT
        )

    @property
    def on_left(self) -> bool:
        """Determine if this corner is on the left side."""
        return (
            self is RectangleCorner.TOP_LEFT
            or self is RectangleCorner.BOTTOM_LEFT
        )

    @property
    def on_right(self) -> bool:
        """Determine if this corner is on the right side."""
        return (
            self is RectangleCorner.TOP_RIGHT
            or self is RectangleCorner.BOTTOM_RIGHT
        )

    @property
    def vertical(self) -> bool:
        """Determine if this vector is vertical."""
        return self.value.vertical

    @property
    def horizontal(self) -> bool:
        """Determine if this vector is horizontal."""
        return self.value.horizontal

    def origin(self, dimensions: Dimensions, location: Point) -> Point:
        """Get the specific corner from a rectangular object."""
        return location.translate(
            self.origin_dx * dimensions.dx, self.origin_dy * dimensions.dy
        )

    @property
    def origin_dx(self) -> float:
        """Get the 'x' component of this corner."""
        return self.value.from_origin.dx

    @property
    def vector_dx(self) -> float:
        """Get the 'x' component of this corner."""
        return self.value.vector.dx

    @property
    def origin_dy(self) -> float:
        """Get the 'y' component of this corner."""
        return self.value.from_origin.dy

    @property
    def vector_dy(self) -> float:
        """Get the 'x' component of this corner."""
        return self.value.vector.dy


TL = RectangleCorner.TOP_LEFT
TR = RectangleCorner.TOP_RIGHT
BL = RectangleCorner.BOTTOM_LEFT
BR = RectangleCorner.BOTTOM_RIGHT
CORNERS = {"tl": TL, "tr": TR, "bl": BL, "br": BR}
