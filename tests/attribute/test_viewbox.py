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

    assert box == ViewBox.from_dict({"width": 100, "height": 100})

    assert box.center == Point(50, 50)
    assert box.key == key
    assert box.value == val
    assert key in box.encode() and val in box.encode()

    assert distance(box.center) == approx(sqrt(2 * 50 * 50))

    # pylint: disable=unnecessary-dunder-call
    assert box.__eq__(5) is NotImplemented
    assert box.center.__eq__(5) is NotImplemented

    grid = box.new_grid(columns=5, rows=5)
    assert grid(1, 1) == Point(20, 20)
    assert grid.adjust(columns=10)
    assert grid.adjust(rows=10)

    box.translate(50, 50)
    assert box.origin == Point(50, 50)
    box.plane.add_point("test", 75, 75)
