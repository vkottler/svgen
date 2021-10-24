"""
svgen - A module for the 'rect' element.
"""

# built-in
from math import isclose
from typing import List

# internal
from svgen.attribute import Attribute, SimpleAttribute
from svgen.attribute.viewbox import ViewBox
from svgen.cartesian import UNITY, Translation
from svgen.cartesian.rectangle import Rectangle
from svgen.element import Element


class Rect(Element):
    """A class for rect elements."""

    def __init__(
        self,
        rect: Rectangle,
        radius_x: float = float(),
        radius_y: float = float(),
    ) -> None:
        """Construct a new rect element."""

        self.rect = rect
        self.location = self.rect.location
        self.dimensions = self.rect.dimensions
        self.radius_x = radius_x
        self.radius_y = radius_y

        attrs: List[Attribute] = []
        attrs += [*self.location.attrs]
        attrs += [*self.dimensions.attrs]

        if self.radius_x != float():
            attrs.append(SimpleAttribute("rx", str(self.radius_x)))
        if self.radius_y != float():
            attrs.append(SimpleAttribute("ry", str(self.radius_y)))

        super().__init__(attributes=attrs)

    @property
    def square(self) -> bool:
        """Determine if this rectangle is square."""

        return self.rect.square

    def to_square(self, scale: float = UNITY) -> "Rect":
        """Convert this rectangle to a square."""

        return Rect(self.rect.to_square(scale), self.radius_x, self.radius_y)

    def translate(self, move: Translation) -> "Rect":
        """Move this rectangle by a given translation."""

        return Rect(self.rect.translate(move), self.radius_x, self.radius_y)

    def scale(
        self, width_scale: float = UNITY, height_scale: float = UNITY
    ) -> "Rect":
        """Scale this rectangle's width and height."""

        return Rect(
            self.rect.scale(width_scale, height_scale),
            self.radius_x,
            self.radius_y,
        )

    def scale_whole(self, scalar: float = UNITY) -> "Rect":
        """Scale width and height of this rectangle equally."""

        return self.scale(scalar, scalar)

    def __eq__(self, other: object) -> bool:
        """Determine if this rectangle is equivalent to another."""

        if not isinstance(other, Rect):
            return NotImplemented
        return (
            self.rect == other.rect
            and isclose(self.radius_x, other.radius_x)
            and isclose(self.radius_y, other.radius_y)
        )


def centered(
    box: ViewBox, width_scale: float = UNITY, height_scale: float = UNITY
) -> Rect:
    """From a viewBox, created a centered-and-scaled rectangle."""

    dimensions = box.dimensions.scale(width_scale, height_scale)
    delta_x = (box.dimensions.width - dimensions.width) / 2.0
    delta_y = (box.dimensions.height - dimensions.height) / 2.0
    Translation(delta_x, delta_y)
    return Rect(
        Rectangle(
            dimensions, box.origin.translate(Translation(delta_x, delta_y))
        )
    )
