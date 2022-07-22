"""
Test the 'color.theme' module.
"""

# module under test
from svgen.cartesian.rectangle import Rectangle
from svgen.color.theme import ColorTheme
from svgen.color.theme.visualize import visualize_theme

# internal
from tests.resources import get_resource


def test_color_theme_basic():
    """Test basic interactions with color themes."""

    theme = ColorTheme.from_path(get_resource("gray.yaml"))

    assert theme["primary.50"] == "f5f5f5"
    assert theme["gray.primary.50"] == "f5f5f5"

    assert theme.resolve("primary.900") == "#000000"
    assert str(theme.resolve("primary.900")) == "#000000"
    assert theme.resolve("primary.900") == theme.resolve("primary.900")

    assert theme.create("primary.900") == theme["primary.900"]
    assert theme.create(theme.create("primary.900")) == theme["primary.900"]

    theme.add("primary.40", "#0f0f0f0f")
    theme.add("primary.40", "#0f0f0f0f")
    assert theme["gray.primary.40"] == "#0f0f0f0f"

    assert visualize_theme(theme, Rectangle.create(100.0, 100.0))
