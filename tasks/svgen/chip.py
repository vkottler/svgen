"""
A script for creating a circuit chip.
"""

# built-in
from collections import defaultdict
from typing import Any

# third-party
from vcorelib.dict import MergeStrategy, merge

# internal
from svgen.attribute.viewbox import ViewBox
from svgen.cartesian import UNITY
from svgen.cartesian.rectangle import Rectangle
from svgen.element import Element
from svgen.shapes.chip import add_chip
from tasks.svgen.lib.symbols import DEFAULT, get_symbol_adder


def compose_index(
    circle_config: dict[str, Any],
    body_config: dict[str, Any],
    pin_config: dict[str, Any],
    symbol_config: dict[str, Any],
    box: Rectangle,
    box_scale: float,
) -> list[Element]:
    """Create the chip based on provided parameters."""

    result: list[Element] = []

    # We could also center the box vertically and horizontally here as
    # well. There's a fair bit more we'd need to do to make
    # centering/padding etc. more ergonomic. At that point it's probably
    # better to use HTML to do that?
    box = box.to_square(box_scale)

    # Create the base chip.
    # chip_elems, body = add_chip(box, circle_config, body_config, pin_config)
    chip_elems, body = add_chip(
        box,
        body_color=body_config["color"],
        pin_color=pin_config["color"],
        circle_color=circle_config.get("color"),
        pin_count=pin_config.get("count", 3),
    )

    # Add the symbol for this chip.
    return (
        result
        + chip_elems
        + get_symbol_adder(symbol_config.get("name", DEFAULT))(
            body.rect, symbol_config
        )
    )


def compose(viewbox: ViewBox, config: dict[str, Any]) -> list[Element]:
    """An example function for composing a document."""

    result: list[Element] = []

    configs = {
        "circle": config.get("circle", {}),
        "body": config["body"],
        "pin": config["pins"],
        "symbol": config.get("symbol", {"name": DEFAULT}),
    }

    box_scale = config.get("scale", UNITY)

    # Apply coordinate-specific configuration data.
    at_coordinate: dict[str, dict[str, dict[str, Any]]] = merge(
        defaultdict(lambda: defaultdict(dict)), config.get("at_coordinate", {})
    )

    for idx, box in viewbox.new_grid(
        columns=config.get("columns", 1), rows=config.get("rows", 1)
    ).enumerate_boxes:
        # Get any coordinate-specific configuration data.
        coord = at_coordinate[str(idx.column)].get(str(idx.row), {})

        curr_configs = {}
        for name, data in configs.items():
            curr_configs[name] = merge(
                data.copy(),
                coord.get(name, {}),
                strategy=MergeStrategy.UPDATE,
            )

        # Create the portion of the document for this coordinate.
        result += compose_index(
            curr_configs["circle"],
            curr_configs["body"],
            curr_configs["pin"],
            curr_configs["symbol"],
            box,
            box_scale,
        )

    return result
