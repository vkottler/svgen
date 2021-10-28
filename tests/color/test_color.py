"""
svgen - Test the 'svgen.color' module.
"""

# module under test
from svgen.color import Color


def test_color_basic():
    """Test basic color interactions."""

    assert Color.from_ctor("rgb(0, 0, 0)") == Color.from_ctor("hsl(0, 0%, 0%)")
    assert Color.from_hex("#FFFFFF").__eq__(5) is NotImplemented
