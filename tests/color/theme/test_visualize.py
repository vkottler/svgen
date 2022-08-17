"""
Test the 'color.theme.visualize' module.
"""

# module under test
from svgen.cartesian.rectangle import Rectangle
from svgen.color.theme.visualize import visualize, visualize_theme


def test_visualize_basic():
    """Test that we can visualize theme data."""

    rect = Rectangle.create(100.0, 100.0)
    assert list(visualize(rect))
    assert list(visualize_theme("blue_gray", rect))
