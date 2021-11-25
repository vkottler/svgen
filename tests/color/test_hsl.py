"""
svgen - Test the 'svgen.color.hsl' module.
"""

# module under test
from svgen.color.hsl import DegreePrimitive, Hsl, hsl, hsla


def test_hsl_basic():
    """Test basic functionality of hsl colors."""

    color = hsl(0, 1.0, 0.5)
    assert color.hue == 0 and color.hue == DegreePrimitive(360)
    assert str(color) == "hsl(0, 100%, 50%)"
    assert Hsl.from_ctor(str(color)) == color


def test_hsla_basic():
    """Test hsl colors with an alpha value."""

    color = hsla(0, 1.0, 0.5, 0.25)
    assert color == Hsl.from_ctor(str(color))
