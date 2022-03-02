"""
svgen - A module for the 'style' attribute.
"""

# built-in
from typing import List, NamedTuple

# internal
from svgen.attribute import Attribute
from svgen.color import Color


class CssProperty(NamedTuple):
    """A class for interacting with css properties."""

    key: str
    value: str

    def __eq__(self, other: object) -> bool:
        """Determine if two css properties are the same."""

        if not isinstance(other, CssProperty):
            return NotImplemented
        return self.key == other.key and self.value == other.value

    @staticmethod
    def color(color: Color, prop: str = "fill") -> "CssProperty":
        """Get a CSS property for a color."""
        return CssProperty(prop, str(color))

    @staticmethod
    def decode(value: str) -> List["CssProperty"]:
        """Create css properties from a string."""

        result: List[CssProperty] = []

        value = value.strip()
        properties = [x.strip() for x in value.split(";")]
        for prop in properties:
            if prop:
                tokens = prop.split(":")
                assert len(tokens) == 2
                key = tokens[0].strip()
                val = tokens[1].strip()
                result.append(CssProperty(key, val))

        return result

    @property
    def encoded(self) -> str:
        """Convert this css property to a string."""
        return f"{self.key}: {self.value}"

    @staticmethod
    def encode(properties: List["CssProperty"]) -> str:
        """Encode a list of css properties to a string."""
        return "; ".join(x.encoded for x in properties)


class Style(Attribute):
    """An interface for style attributes."""

    def __init__(self, properties: List[CssProperty] = None) -> None:
        """Construct a new style attribute."""

        if properties is None:
            properties = []
        self.properties: List[CssProperty] = properties

    def __eq__(self, other: object) -> bool:
        """Determine if two style attributes are the same."""

        if not isinstance(other, Style):
            return NotImplemented

        result = self.key == other.key
        result = result and len(self.properties) == len(other.properties)
        if result:
            props = sorted(self.properties)
            other_props = sorted(other.properties)
            for idx, prop in enumerate(props):
                if not result:
                    break
                result = result and prop == other_props[idx]

        return result

    def add_color(self, color: Color, prop: str = "fill") -> None:
        """Set a style property to a color."""
        self.properties.append(CssProperty.color(color, prop))

    @property
    def value(self) -> str:
        """Get the string value for this attribute."""
        return CssProperty.encode(self.properties)

    @staticmethod
    def decode(key: str, value: str) -> Attribute:
        """Create this attribute from a string."""

        assert key == "style"
        return Style(CssProperty.decode(value))
