"""
svgen - Test the 'element.rect' module.
"""

# third-party
from pytest import approx

# module under test
from svgen.element.rect import Rect
from svgen.cartesian.rectangle import Rectangle, Dimensions


def test_rect_basic():
    """Test the rect interface."""

    rect = Rect(Rectangle(Dimensions(100.0, 100.0)), 1.0, 1.0)
    assert approx(rect.dimensions.attrs.width_val, 100)
    assert approx(rect.dimensions.attrs.height_val, 100)
    assert approx(rect.location.attrs.x_val, 0)
    assert approx(rect.location.attrs.y_val, 0)
