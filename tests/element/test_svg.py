"""
svgen - Test the 'element.svg' module.
"""

# module under test
from svgen.attribute import XMLNS, SimpleAttribute
from svgen.attribute.viewbox import ViewBox
from svgen.element.svg import Svg


def test_svg_basic():
    """Test the svg interface."""

    svg = Svg(ViewBox.decode("viewBox", "0 0 100 100"))
    assert (
        svg.encode_str(newlines=False)
        == '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" />'
    )

    assert XMLNS == SimpleAttribute.decode(
        "xmlns", "http://www.w3.org/2000/svg"
    )
