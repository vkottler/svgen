"""
svgen - Test the 'element' module.
"""

# module under test
from svgen.element import Element
from svgen.attribute.viewbox import ViewBox


def test_element_basic():
    """Test the element interface."""

    # Test an element with no content.
    elem = Element("svg")
    assert elem.encode_str(newlines=False) == "<svg />"

    # Test an element with some content.
    elem = Element("svg", "test")
    assert elem.encode_str(newlines=False) == "<svg>test</svg>"
    assert elem.encode_str() == "<svg>\n  test\n</svg>\n"

    # Test an element with an attribute.
    box = ViewBox.decode("viewBox", "0 0 100 100")
    elem = Element("svg", "test", [box])
    assert (
        elem.encode_str(newlines=False)
        == '<svg viewBox="0 0 100 100">test</svg>'
    )

    # Test an element with children.
    elem.children.append(Element("svg"))
    assert (
        elem.encode_str(newlines=False)
        == '<svg viewBox="0 0 100 100">test<svg /></svg>'
    )
    assert (
        elem.encode_str()
        == '<svg viewBox="0 0 100 100">\n  test\n  <svg />\n</svg>\n'
    )
