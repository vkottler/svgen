"""
A module for resolving colors.
"""

# internal
from svgen.color import Color, Colorlike
from svgen.color.theme.manager import THEMES, ColorThemeManager


def get_color(key: Colorlike, manager: ColorThemeManager = None) -> Color:
    """Resolve a color using the theme manager."""
    if manager is None:
        manager = THEMES
    return manager[key].color
