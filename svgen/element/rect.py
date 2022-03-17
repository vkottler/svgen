"""
svgen - A module for the 'rect' element.
"""

# built-in
from math import isclose
from typing import Union

# internal
from svgen.attribute import PossibleAttributes, SimpleAttribute, attributes
from svgen.attribute.viewbox import ViewBox
from svgen.cartesian import UNITY, Translation
from svgen.cartesian.rectangle import Rectangle
from svgen.color import Color
from svgen.element import Element


class Rect(Element):
    """A class for rect elements."""

    def __init__(
        self,
        rect: Rectangle,
        rx: float = float(),
        ry: float = float(),
        attrs: PossibleAttributes = None,
        **extra,
    ) -> None:
        """Construct a new rect element."""

        self.rect = rect
        self.location = self.rect.location
        self.dimensions = self.rect.dimensions
        self.rx = rx
        self.ry = ry

        real_attrs = attributes(attrs)
        real_attrs += [*self.location.attrs]
        real_attrs += [*self.dimensions.attrs]

        if self.rx != float():
            real_attrs.append(SimpleAttribute("rx", str(self.rx)))
        if self.ry != float():
            real_attrs.append(SimpleAttribute("ry", str(self.ry)))

        super().__init__(attrib=real_attrs, **extra)

    @property
    def square(self) -> bool:
        """Determine if this rectangle is square."""

        return self.rect.square

    def to_square(self, scale: float = UNITY) -> "Rect":
        """Convert this rectangle to a square."""

        return Rect(self.rect.to_square(scale), self.rx, self.ry)

    def translate(self, move: Translation) -> "Rect":
        """Move this rectangle by a given translation."""

        return Rect(self.rect.translate(move), self.rx, self.ry)

    def scale(
        self, width_scale: float = UNITY, height_scale: float = UNITY
    ) -> "Rect":
        """Scale this rectangle's width and height."""

        return Rect(
            self.rect.scale(width_scale, height_scale),
            self.rx,
            self.ry,
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
            and isclose(self.rx, other.rx)
            and isclose(self.ry, other.ry)
        )


def centered(
    box: ViewBox,
    width_scale: float = UNITY,
    height_scale: float = UNITY,
    color: Union[Color, str] = None,
    prop: str = "fill",
    **kwargs,
) -> Rect:
    """From a viewBox, created a centered-and-scaled rectangle."""

    dimensions = box.dimensions.scale(width_scale, height_scale)
    delta_x = (box.dimensions.width - dimensions.width) / 2.0
    delta_y = (box.dimensions.height - dimensions.height) / 2.0

    result = Rect(
        Rectangle(
            dimensions, box.origin.translate(Translation(delta_x, delta_y))
        ),
        **kwargs,
    )

    if color is not None:
        result.style.add_color(color, prop)
    return result
