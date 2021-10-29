"""
svgen - Test the 'svgen.color.rgb' module.
"""

# built-in
from math import isclose

# module under test
from svgen.color.numbers import css_number_to_ratio
from svgen.color.rgb import Rgb, rgb, rgba


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


def test_rgba_basic():
    """Test rgb colors with an alpha value."""

    assert rgb(256, 256, 256) == rgba(255, 255, 255, 1.0)
    assert rgba(255, 255, 255, "50%").alpha == 0.5

    color = rgba(128, 128, 128, 0.25)
    assert color.alpha.__eq__(5) is NotImplemented

    assert Rgb.from_ctor("rgba(128, 128, 128, 25%)") == color
    assert Rgb.from_ctor("rgba(128, 128, 128, 26%)") != color
    assert color.rgba == "rgba(128, 128, 128, 0.25)"

    assert Rgb.from_hex("#80808040") == color

    assert isclose(css_number_to_ratio(255), 1.0)
