"""
svgen - Test the 'element' module.
"""

# built-in
from os import linesep
from xml.etree import ElementTree as et

# module under test
from svgen.attribute.viewbox import ViewBox
from svgen.element import Element
from svgen.element.svg import Svg


def test_element_basic():
    """Test the element interface."""

    # Test an element with no content.
    elem = Element("svg")
    assert elem.encode_str(newlines=False) == "<svg />"

    elem.allow_no_end_tag = False
    assert elem.encode_str(newlines=False) == "<svg></svg>"

    # Test an element with some content.
    elem = Element("svg", "test")
    assert elem.encode_str(newlines=False) == "<svg>test</svg>"
    assert elem.encode_str() == f"<svg>{linesep}  test{linesep}</svg>{linesep}"

    # Test an element with an attribute.
    box = ViewBox.decode("viewBox", "0 0 100 100")
    elem = Element("svg", "test", [box])
    assert (
        elem.encode_str(newlines=False)
        == '<svg viewBox="0 0 100 100">test</svg>'
    )

    # Test an element with children.
    elem.children.append(Element("svg", a="b"))
    assert (
        elem.encode_str(newlines=False)
        == '<svg viewBox="0 0 100 100">test<svg a="b" /></svg>'
    )
    assert elem.encode_str() == (
        f'<svg viewBox="0 0 100 100">{linesep}  '
        f'test{linesep}  <svg a="b" />{linesep}</svg>{linesep}'
    )

    elem["a"] = 1
    elem["b"] = 2
    elem["c"] = 3

    assert elem["a"] == "1"
    assert elem["b"] == "2"
    assert elem["c"] == "3"

    elem["a"] += "2"
    assert elem["a"] == "12"


def test_element_xml():
    """Test that we can get XML elements from elements in this package."""

    elem = Svg(ViewBox.decode("viewBox", "0 0 100 100"))

    rect = Element("rect")
    elem.children.append(rect)

    assert et.tostring(elem.xml, encoding="unicode") == (
        '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
        "<rect /></svg>"
    )

    rect.booleans.add("hidden")
    rect.text = "Hello, world!"
    assert (
        rect.encode_str(newlines=False) == "<rect hidden>Hello, world!</rect>"
    )
