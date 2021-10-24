"""
svgen - A module for interacting with rectangular entities.
"""

# built-in
from typing import NamedTuple

# internal
from svgen.attribute import SimpleAttribute
from svgen.cartesian import DEFAULT, Point


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


class Rectangle(NamedTuple):
    """A definition of a rectangle."""

    dimensions: Dimensions
    location: Point = DEFAULT
