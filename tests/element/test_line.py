"""
svgen - Test the 'element.line' module.
"""

from svgen.cartesian.mutate import Translation

# module under test
from svgen.cartesian.point import Point
from svgen.element.line import line


def test_line_basic():
    """Test the line interface."""

    lin = line(1.0, 1.0)
    translated = lin.translate(Translation(1.0, 1.0))
    assert translated.p1 == Point(1.0, 1.0)
    assert translated.p2 == Point(2.0, 2.0)
