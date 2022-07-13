"""
svgen - A module for interacting with rectangular entities.
"""

# built-in
from enum import Enum
from math import isclose
from typing import NamedTuple

# internal
from svgen.attribute import SimpleAttribute
from svgen.cartesian import DEFAULT, UNITY, VECTORS, Point, Translation


class DimensionAttrs(NamedTuple):
    """A grouping for 'width' and 'height' attributes."""

    width: SimpleAttribute
    height: SimpleAttribute

    @property
    def width_val(self) -> float:
        """Get this 'width' value for these dimensions."""

        return float(self.width.value)

    @property
    def height_val(self) -> float:
        """Get the 'height' value for these dimensions."""

        return float(self.height.value)


class Dimensions(NamedTuple):
    """A set of dimensions describing a rectangular entity."""

    width: float
    height: float

    def __str__(self) -> str:
        """Get this instance as a string."""
        return f"width={self.width}, height={self.height})"

    def __hash__(self) -> int:
        """Get a suitable hash value for this instance."""
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        """Determine if these dimensions are equivalent to another set."""

        if not isinstance(other, Dimensions):
            return NotImplemented
        return isclose(self.width, other.width) and isclose(
            self.height, other.height
        )

    @property
    def dx(self) -> float:
        """An alias for width."""
        return self.width

    @property
    def dy(self) -> float:
        """An alias for height."""
        return self.height

    @property
    def width_attr(self) -> SimpleAttribute:
        """Get the 'width' attribute for these dimensions."""

        return SimpleAttribute("width", str(self.width))

    @property
    def height_attr(self) -> SimpleAttribute:
        """Get the 'height' attribute for these dimensions."""

        return SimpleAttribute("height", str(self.height))

    @property
    def attrs(self) -> DimensionAttrs:
        """Get the 'width' and 'height' attributes for these dimensions."""

        return DimensionAttrs(self.width_attr, self.height_attr)

    @property
    def square(self) -> bool:
        """Determine if these dimensions are square."""

        return isclose(self.width, self.height)

    def scale(
        self, width_scale: float = UNITY, height_scale: float = UNITY
    ) -> "Dimensions":
        """Scale these dimensions."""

        return Dimensions(self.width * width_scale, self.height * height_scale)

    def to_square(self, scale: float = UNITY) -> "Dimensions":
        """Convert these dimensions to a scaled square."""

        length = min(self.width, self.height)
        return Dimensions(length, length).scale(scale, scale)


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
        return (
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


class Rectangle(NamedTuple):
    """A definition of a rectangle."""

    dimensions: Dimensions
    location: Point = DEFAULT

    def __eq__(self, other: object) -> bool:
        """Determine if this rectangle is equivalent to another."""

        if not isinstance(other, Rectangle):
            return NotImplemented
        return (
            self.dimensions == other.dimensions
            and self.location == other.location
        )

    @property
    def width(self) -> float:
        """Get the width of this rectangle."""
        return self.dimensions.width

    @property
    def height(self) -> float:
        """Get the height of this rectangle.."""
        return self.dimensions.height

    @property
    def square(self) -> bool:
        """Determine if this rectangle is square."""
        return self.dimensions.square

    def translate(self, move: Translation) -> "Rectangle":
        """Move a rectangle by a given translation."""
        return Rectangle(self.dimensions, self.location.translate(move))

    def scale(
        self, width_scale: float = UNITY, height_scale: float = UNITY
    ) -> "Rectangle":
        """Scale this rectangle's width and height."""
        return Rectangle(
            self.dimensions.scale(width_scale, height_scale), self.location
        )

    def scale_whole(self, scalar: float = UNITY) -> "Rectangle":
        """Scale width and height of this rectangle equally."""
        return self.scale(scalar, scalar)

    def to_square(self, scale: float = UNITY) -> "Rectangle":
        """Convert this rectangle to a square."""
        return Rectangle(self.dimensions.to_square(scale), self.location)

    @staticmethod
    def create(
        width: float, height: float, point: Point = DEFAULT
    ) -> "Rectangle":
        """Create a rectangle from simple parameters."""
        return Rectangle(Dimensions(width, height), point)

    def corner(self, corner: RectangleCorner) -> Point:
        """Get a specific corner of a rectangle."""
        return corner.origin(self.dimensions, self.location)

    @property
    def top_left(self) -> Point:
        """Get the top left corner point."""
        return self.corner(RectangleCorner.TOP_LEFT)

    @property
    def top_right(self) -> Point:
        """Get the top right corner point."""
        return self.corner(RectangleCorner.TOP_RIGHT)

    @property
    def bottom_left(self) -> Point:
        """Get the bottom left corner point."""
        return self.corner(RectangleCorner.BOTTOM_LEFT)

    @property
    def bottom_right(self) -> Point:
        """Get the bottom right corner point."""
        return self.corner(RectangleCorner.BOTTOM_RIGHT)
