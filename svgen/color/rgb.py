"""
svgen - Common interfaces for rgb colors. See also:

        https://www.w3schools.com/colors/colors_rgb.asp
"""

# built-in
from typing import NamedTuple


class RgbPrimitive(int):
    """An integer type for rgb values."""

    def __new__(cls, val: int) -> "RgbPrimitive":
        """Create a new primitive value for an rgb color."""

        val = max(val, 0)
        val = min(val, 255)
        return super().__new__(cls, val)

    def __str__(self) -> str:
        """Get this color value as a hex string."""

        return f"{int(self):X}"


class Rgb(NamedTuple):
    """A definition of an rgb color."""

    red: RgbPrimitive
    green: RgbPrimitive
    blue: RgbPrimitive

    def __str__(self) -> str:
        """Get this color as a hex string."""

        return f"#{self.red}{self.green}{self.blue}"

    @property
    def rgb(self) -> str:
        """Get this color as an 'rgb' constructor."""

        return f"rgb({int(self.red)}, {int(self.green)}, {int(self.blue)})"

    @staticmethod
    def from_hex(value: str) -> "Rgb":
        """Get an rgb color from a hex string."""

        value = value.replace("#", "")
        value = value.strip()
        assert len(value) == 6
        return Rgb(
            RgbPrimitive(int(value[0:2], 16)),
            RgbPrimitive(int(value[2:4], 16)),
            RgbPrimitive(int(value[4:6], 16)),
        )

    @staticmethod
    def from_ctor(value: str) -> "Rgb":
        """Get an rgb color from a constructor string."""

        value = value.strip()
        if value.startswith("rgb("):
            value = value.replace("rgb(", "")
        if value.endswith(")"):
            value = value.replace(")", "")
        colors = [x.strip() for x in value.split(",")]
        assert len(colors) == 3
        return Rgb(
            RgbPrimitive(int(colors[0])),
            RgbPrimitive(int(colors[1])),
            RgbPrimitive(int(colors[2])),
        )


def rgb(red: int, green: int, blue: int) -> Rgb:
    """Create a new RGB color."""

    return Rgb(RgbPrimitive(red), RgbPrimitive(green), RgbPrimitive(blue))
