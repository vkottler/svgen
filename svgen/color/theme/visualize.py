"""
A module for visualizing color themes.
"""

# built-in
from typing import Iterator

# internal
from svgen.cartesian.rectangle import Rectangle
from svgen.cartesian.rectangle.grid import RectangleGrid
from svgen.color.theme import ColorTheme
from svgen.color.theme.manager import THEMES, ColorThemeManager
from svgen.element.rect import Rect


def visualize_theme(theme: ColorTheme, rect: Rectangle) -> Iterator[Rect]:
    """
    Create filled rectangle elements for this theme inside another
    rectangle.
    """

    for box, color in zip(
        RectangleGrid(rect, theme.size, 1).boxes,
        theme.data.values(),
    ):
        curr = Rect(box)
        curr.style.add_color(color, "fill")
        yield curr


def visualize(
    rect: Rectangle, manager: ColorThemeManager = None
) -> Iterator[Rect]:
    """Visualize all managed themes within a provided rectangle."""

    if manager is None:
        manager = THEMES

    for box, theme in zip(
        RectangleGrid(rect, 1, manager.size).boxes, manager.data.values()
    ):
        yield from visualize_theme(theme, box)
