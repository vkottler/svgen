"""
svgen - Test the 'element.circle' module.
"""

# third-party
from pytest import approx

# module under test
from svgen.cartesian.circle import Circle as CartCircle
from svgen.element.circle import Circle


def test_circle_basic():
    """Test the circle interface."""

    circle = Circle(CartCircle(5.0))
    assert approx(circle.raw.attrs.radius_val, 5)
