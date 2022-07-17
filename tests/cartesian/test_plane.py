"""
Test the 'cartesian.plane' module.
"""

from svgen.cartesian.plane import RectangleGrid

# module under test
from svgen.cartesian.point import Point
from svgen.cartesian.rectangle import Rectangle


def test_cartesian_plane_grid_boxes():
    """Test that we can correctly create boxes from a rectangle grid."""

    rect = Rectangle.create(100.0, 100.0)
    grid = RectangleGrid(rect, 10, 10)
    assert grid(1, 1) == Point(10.0, 10.0)
    assert grid.box(1, 1) == Rectangle.create(10.0, 10.0, Point(10.0, 10.0))

    points = list(grid.points)
    assert len(points) == 100
    assert points[0] == Point(0.0, 0.0)
    assert points[1] == Point(10.0, 0.0)
    assert points[-1] == Point(90.0, 90.0)
    assert len(list(grid.boxes)) == 100
