"""
svgen - A module for working with colors.
"""

# built-in
from typing import NamedTuple

# internal
from svgen.color.conversion import rgb_to_hsl, hsl_to_rgb
from svgen.color.hsl import Hsl
from svgen.color.rgb import Rgb


class Color(NamedTuple):
    """A definition of a color."""

    rgb: Rgb
    hsl: Hsl

    def __eq__(self, other: object) -> bool:
        """Determine if two colors are equal."""

        if not isinstance(other, Color):
            return NotImplemented
        return self.rgb == other.rgb or self.hsl == other.hsl

    @classmethod
    def from_rgb(cls, color: Rgb) -> "Color":
        """Create a color from an rgb object."""

        return cls(color, rgb_to_hsl(color))

    @classmethod
    def from_hex(cls, value: str) -> "Color":
        """Create a color from a hex value."""

        return cls.from_rgb(Rgb.from_hex(value))

    @classmethod
    def from_hsl(cls, color: Hsl) -> "Color":
        """Create a color from an hsl object."""

        return cls(hsl_to_rgb(color), color)

    @classmethod
    def from_ctor(cls, value: str) -> "Color":
        """Create a color from an hsl or rgb constructor string."""

        assert "rgb" in value or "hsl" in value
        if "rgb" in value:
            return cls.from_rgb(Rgb.from_ctor(value))
        return cls.from_hsl(Hsl.from_ctor(value))
