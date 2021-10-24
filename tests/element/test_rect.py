"""
svgen - Test the 'element.rect' module.
"""

# third-party
from pytest import approx

# module under test
from svgen.element.rect import Rect
from svgen.cartesian import Translation, Point
from svgen.cartesian.rectangle import Rectangle, Dimensions


def test_rect_basic():
    """Test the rect interface."""

    rect = Rect(Rectangle(Dimensions(100.0, 100.0)), 1.0, 1.0)
    assert approx(rect.dimensions.attrs.width_val, 100)
    assert approx(rect.dimensions.attrs.height_val, 100)
    assert approx(rect.location.attrs.x_val, 0)
    assert approx(rect.location.attrs.y_val, 0)


def test_rect_mutate():
    """Test the correctness of various rectangle mutations."""

    full = Dimensions(100.0, 100.0)
    half = Dimensions(50.0, 50.0)
    full_rect = Rect(Rectangle(full), 1.0, 1.0)
    half_rect = Rect(Rectangle(half), 1.0, 1.0)

    assert full_rect != half_rect
    assert half_rect.scale_whole(2.0) == full_rect

    assert full_rect.to_square() == full_rect
    assert half_rect.to_square() == half_rect
    assert full_rect.__eq__(5) is NotImplemented
    assert full_rect.rect.__eq__(5) is NotImplemented
    assert full_rect.rect.dimensions.__eq__(5) is NotImplemented
    assert full_rect.square

    assert full_rect.translate(Translation(2.0, 2.0)) == Rect(
        Rectangle(full, Point(2.0, 2.0)), 1.0, 1.0
    )

    assert full_rect.rect.scale_whole(0.5) == half_rect.rect
