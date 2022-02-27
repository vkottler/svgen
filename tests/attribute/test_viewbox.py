"""
svgen - Test the 'attribute.viewbox' module.
"""

# built-in
from math import sqrt

# third-party
from pytest import approx

# module under test
from svgen.attribute.viewbox import ViewBox
from svgen.cartesian import Point, distance


def test_viewbox_basic():
    """Test basic viewBox functionality."""

    key = "viewBox"
    val = "0 0 100 100"
    box = ViewBox.decode(key, val)
    assert box == ViewBox.decode(key, val)
    assert box.__eq__(5) is NotImplemented

    assert box.center == Point(50, 50)
    assert box.key == key
    assert box.value == val
    assert key in box.encode() and val in box.encode()

    assert distance(box.center) == approx(sqrt(2 * 50 * 50))

    assert box.center.__eq__(5) is NotImplemented
