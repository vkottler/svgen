"""
A module for obtaining various symbol drawing implementations.
"""

# built-in
from typing import Any, Callable, List

# internal
from svgen.cartesian.rectangle import Rectangle
from svgen.element import Element
from tasks.svgen.lib.symbols.text import add_symbol as add_text
from tasks.svgen.lib.symbols.vdoer import add_symbol as add_vdoer

SymbolAdder = Callable[[Rectangle, dict[str, Any]], List[Element]]
DEFAULT = "vdoer"


def get_symbol_adder(name: str) -> SymbolAdder:
    """Get a symbol implementation by name."""
    return {DEFAULT: add_vdoer, "text": add_text}.get(name, add_vdoer)
