"""
A module implementing cartesian object mutations.
"""

# built-in
from math import cos, degrees, isclose, radians, sin
from typing import NamedTuple, Union


class Angle(NamedTuple):
    """A definition of angle attributes."""

    degrees: float
    radians: float
    sin: float
    cos: float

    @staticmethod
    def from_degrees(val: float) -> "Angle":
        """Create an angle from a degree value."""
        return Angle.from_radians(radians(val))

    @staticmethod
    def from_radians(val: float) -> "Angle":
        """Create an angle from a radian value."""
        return Angle(degrees(val), val, sin(val), cos(val))


ANGLES = {
    "quarter": Angle.from_degrees(90),
    "half": Angle.from_degrees(180),
    "three_quarter": Angle.from_degrees(270),
}


class Translation(NamedTuple):
    """A definition of a translation in a Cartesian coordinate system."""

    dx: float = 0.0
    dy: float = 0.0

    def __eq__(self, other) -> bool:
        """Test if two translations are equivalent."""
        return isclose(self.dx, other.dx, abs_tol=1e-12) and isclose(
            self.dy, other.dy, abs_tol=1e-12
        )

    def rotate(self, angle: Angle = ANGLES["quarter"]) -> "Translation":
        """Rotate this translation vector by some angle."""
        return Translation(
            self.dx * angle.cos - self.dy * angle.sin,
            self.dx * angle.sin + self.dy * angle.cos,
        )

    @staticmethod
    def normalize(
        dx: Union["Translation", float], *args, **kwargs
    ) -> "Translation":
        """Normalize input data into a translation."""
        if isinstance(dx, Translation):
            return dx
        return Translation(dx, *args, **kwargs)


# Common translations.
UP = Translation(0.0, -1.0)
DOWN = Translation(0.0, 1.0)
LEFT = Translation(-1.0, 0.0)
RIGHT = Translation(1.0, 0.0)
VECTORS = {"up": UP, "down": DOWN, "left": LEFT, "right": RIGHT}
