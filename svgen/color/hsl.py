"""
svgen - Common interfaces for hsl colors. See also:

        https://www.w3schools.com/colors/colors_hsl.asp
"""

# built-in
from typing import NamedTuple

# internal
from svgen.color.alpha import DEFAULT, Alpha
from svgen.color.numbers import parse_ctor


class DegreePrimitive(int):
    """
    A class to manage integer primitives for degrees within a 0 and 360 range.
    """

    def __new__(cls, val: int) -> "DegreePrimitive":
        """Construct a new degree value."""
        return super().__new__(cls, val % 360)


class PercentPrimitive(int):
    """A class for integer percentages."""

    def __new__(cls, val: int) -> "PercentPrimitive":
        """Create a new percentage value."""
        val = max(val, 0)
        val = min(val, 100)
        return super().__new__(cls, val)

    def __str__(self) -> str:
        """Get this percentage as a string."""
        return f"{int(self)}%"

    @property
    def ratio(self) -> float:
        """Get this percentage as a ratio between 0 and 1."""
        return float(self) / 100.0


class Hsl(NamedTuple):
    """A definition of an hsl color."""

    hue: DegreePrimitive
    saturation: PercentPrimitive
    lightness: PercentPrimitive
    alpha: Alpha = DEFAULT

    def __str__(self) -> str:
        """Convert this hsl color to a string."""

        if self.alpha == DEFAULT:
            return f"hsl({self.hue}, {self.saturation}, {self.lightness})"
        return (
            f"hsla({self.hue}, {self.saturation}, "
            f"{self.lightness}, {self.alpha})"
        )

    @staticmethod
    def from_ctor(value: str) -> "Hsl":
        """Get an hsl color from a constructor string."""

        colors = parse_ctor(value, "hsl", "a")
        assert len(colors) == 3 or len(colors) == 4

        # Parse the alpha value if present.
        alpha = DEFAULT
        if len(colors) == 4:
            alpha = Alpha(float(colors[3]))

        colors[1] = colors[1].replace("%", "")
        colors[2] = colors[2].replace("%", "")
        return Hsl(
            DegreePrimitive(int(colors[0])),
            PercentPrimitive(int(colors[1])),
            PercentPrimitive(int(colors[2])),
            alpha,
        )


def hsl(hue: int, saturation: float, lightness: float) -> Hsl:
    """Create a new hsl color."""

    return Hsl(
        DegreePrimitive(hue),
        PercentPrimitive(round(saturation * 100.0)),
        PercentPrimitive(round(lightness * 100.0)),
    )


def hsla(hue: int, saturation: float, lightness: float, alpha: float) -> Hsl:
    """Create a new hsl color with a transparency value."""

    return Hsl(
        DegreePrimitive(hue),
        PercentPrimitive(round(saturation * 100.0)),
        PercentPrimitive(round(lightness * 100.0)),
        Alpha(alpha),
    )
