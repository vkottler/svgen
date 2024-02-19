"""
Test the 'element.html' module.
"""

# module under test
from svgen.element.html import Html


def test_html_basic():
    """Test basic interactions with an HTML element."""

    doc = Html("test")
    assert doc.encode_str()
