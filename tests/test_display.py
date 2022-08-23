"""
Test the 'display' module.
"""

from svgen.attribute.viewbox import ViewBox

# module under test
from svgen.display import AspectRatio, common_sizes


def test_aspect_ratio_basic():
    """Test basic functionality of aspect ratios."""

    assert str(AspectRatio.create("4:3")) == "4:3"
    assert AspectRatio(2, 1).landscape
    assert AspectRatio(1, 2).portrait
    assert AspectRatio(1, 2).rotate().landscape
    assert list(common_sizes("5:4"))
    assert list(common_sizes("4:5"))
    assert list(common_sizes(ViewBox(0, 0, 800, 600)))
