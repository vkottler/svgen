"""
svgen - A module for the viewBox attribute.
"""

# built-in
from typing import NamedTuple

# internal
from svgen.attribute import Attribute
from svgen.cartesian import Point


class ViewBoxData(NamedTuple):
    """Primitive data for a viewBox attribute."""

    min_x: int
    min_y: int
    width: int
    height: int

    @property
    def center(self) -> Point:
        """Get the center point for this viewBox."""

        return Point(
            self.min_x + (float(self.width) / 2.0),
            self.min_y + (float(self.height) / 2.0),
        )


class ViewBox(Attribute):
    """An interface for viewBox attributes."""

    def __init__(
        self, min_x: int, min_y: int, width: int, height: int
    ) -> None:
        """Construct a new viewBox."""

        self.data = ViewBoxData(min_x, min_y, width, height)

    @property
    def key(self) -> str:
        """Get the string key for this attribute."""

        return "viewBox"

    @property
    def value(self) -> str:
        """Get the string value for this attribute."""

        return (
            f"{self.data.min_x} {self.data.min_y} "
            f"{self.data.width} {self.data.height}"
        )

    @property
    def center(self) -> Point:
        """Get the center point for this viewBox."""

        return self.data.center

    @staticmethod
    def decode(key: str, value: str) -> Attribute:
        """Create this attribute from a string."""

        assert key == "viewBox"
        args = [int(x) for x in value.split()]
        assert len(args) == 4
        return ViewBox(*args)
