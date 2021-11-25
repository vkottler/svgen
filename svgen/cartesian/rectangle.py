"""
svgen - A module for interacting with rectangular entities.
"""

# built-in
from math import isclose
from typing import NamedTuple

# internal
from svgen.attribute import SimpleAttribute
from svgen.cartesian import DEFAULT, UNITY, Point, Translation


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

    def __eq__(self, other: object) -> bool:
        """Determine if these dimensions are equivalent to another set."""

        if not isinstance(other, Dimensions):
            return NotImplemented
        return isclose(self.width, other.width) and isclose(
            self.height, other.height
        )

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
