"""
svgen - Test the 'attribute.style' module.
"""

# module under test
from svgen.attribute.style import Style, CssProperty


def test_style_basic():
    """Test basic style-attribute functionality."""

    props = [CssProperty("margin", "15px")]
    assert CssProperty.decode("margin: 15px;") == props
    assert CssProperty.decode("margin: 15px;")[0] == props[0]
    assert props[0].__eq__(5) is NotImplemented

    props.append(CssProperty("line-height", "1.5"))
    assert CssProperty.decode("margin: 15px; line-height: 1.5") == props

    assert CssProperty.encode(props) == "margin: 15px; line-height: 1.5"

    style = Style(props)
    new_props = props.copy()
    new_props.reverse()
    assert Style() == Style()
    assert style == Style(new_props)
    assert style != Style([props[0]] + [CssProperty("margin", "0")])
    assert style.__eq__(5) is NotImplemented

    assert Style.decode("style", style.value) == style
