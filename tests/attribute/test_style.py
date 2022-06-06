"""
svgen - Test the 'attribute.style' module.
"""

# module under test
from svgen.attribute import SimpleAttribute, attributes
from svgen.attribute.style import CssProperty, Style
from svgen.color import Color


def test_attribute_basic():
    """Test basic functionality of the attribute interfaces."""

    assert attributes({"a": 1})
    assert attributes(SimpleAttribute("a", 1))


def test_style_basic():
    """Test basic style-attribute functionality."""

    props = [CssProperty("margin", "15px")]
    assert CssProperty.decode("margin: 15px;") == props
    assert CssProperty.decode("margin: 15px;")[0] == props[0]

    # pylint: disable=unnecessary-dunder-call
    assert props[0].__eq__(5) is NotImplemented

    props.append(CssProperty("line-height", "1.5"))
    assert CssProperty.decode("margin: 15px; line-height: 1.5") == props

    assert CssProperty.encode(props) == "margin: 15px; line-height: 1.5"

    style = Style(props)
    assert style.__eq__(5) is NotImplemented
    new_props = props.copy()
    new_props.reverse()
    assert Style() == Style()
    assert style == Style(new_props)
    assert style != Style([props[0]] + [CssProperty("margin", "0")])

    assert Style.decode("style", style.value) == style
    style.add_color(Color.from_ctor("purple"))
    style.add({"stroke": "red"})
    style.add(CssProperty("foo", "bar"))
