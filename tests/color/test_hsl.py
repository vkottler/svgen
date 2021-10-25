"""
svgen - Test the 'svgen.color.hsl' module.
"""

# module under test
from svgen.color.hsl import hsl, Hsl, DegreePrimitive


def test_hsl_basic():
    """Test basic functionality of hsl colors."""

    color = hsl(0, 1.0, 0.5)
    assert color.hue == 0 and color.hue == DegreePrimitive(360)
    assert str(color) == "hsl(0, 100%, 50%)"
    assert Hsl.from_ctor(str(color)) == color
