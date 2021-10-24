"""
svgen - Test the 'element.circle' module.
"""

# third-party
from pytest import approx

# module under test
from svgen.attribute.viewbox import ViewBox
from svgen.cartesian import Point
from svgen.cartesian.circle import Circle as CartCircle
from svgen.element.circle import Circle, centered


def test_circle_basic():
    """Test the circle interface."""

    circle = Circle(CartCircle(5.0))
    assert approx(circle.raw.attrs.radius_val, 5)


def test_circle_centered():
    """Test that a circle centered in a viewBox is created correctly."""

    # Test a full-scale circle.
    box = ViewBox(0, 0, 100, 100)
    circle = centered(box)
    assert approx(circle.raw.radius, 50)
    assert circle.raw.center == Point(50, 50)

    # Test a half-scale circle.
    circle = centered(box, 0.5)
    assert approx(circle.raw.radius, 25)
    assert circle.raw.center == Point(50, 50)

    # Test a non-square viewBox.
    box = ViewBox(0, 0, 100, 50)
    circle = centered(box)
    assert approx(circle.raw.radius, 25)
    assert circle.raw.center == Point(50, 25)
