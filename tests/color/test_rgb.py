"""
svgen - Test the 'svgen.color.rgb' module.
"""

# module under test
from svgen.color.rgb import Rgb, rgb


def test_rgb_basic():
    """Test basic functionality of rgb colors."""

    color = rgb(256, 256, 256)
    assert color.red == 255
    assert color.green == 255
    assert color.blue == 255
    assert str(color.red) == "FF"
    assert str(color) == "#FFFFFF"
    assert color.rgb == "rgb(255, 255, 255)"
    assert Rgb.from_hex(str(color)) == color
    assert Rgb.from_ctor(color.rgb) == color
