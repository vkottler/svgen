"""
A sample svgen script.
"""

# built-in
from typing import Any

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.color.theme.visualize import visualize, visualize_theme
from svgen.element import Element
from svgen.element.text import Text


def compose(viewbox: ViewBox, config: dict[str, Any]) -> list[Element]:
    """An example function for composing a document."""

    theme = config.get("theme")
    if theme:
        result: list[Element] = []
        for rect in visualize_theme(theme, viewbox.box, columns=False):
            text = Text("", rect)

            # Set text.
            text.text = f"{rect.fill_color} (text: {text.fill_color})"

            # Improve sizing.
            text["font-size"] = "0.33em"
            text["font-family"] = "monospace"

            # Add elements.
            result.append(rect)
            result.append(text)

        return result

    return list(visualize(viewbox.box))
