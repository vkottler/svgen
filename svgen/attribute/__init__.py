"""
svgen - A module for XML-style attribute interfaces.
"""

# built-in
from abc import ABC, abstractmethod


class Attribute(ABC):
    """An interface for an XML-style attribute."""

    def __eq__(self, other: object) -> bool:
        """Determine if two attributes are the same."""

        if not isinstance(other, type(self)):
            return NotImplemented
        return self.key == other.key and self.value == other.value

    @property
    def key(self) -> str:
        """Get the string key for this attribute."""

        if hasattr(self, "name"):
            return getattr(self, "name")

        key = type(self).__name__
        return key[0].lower() + key[1:]

    @property
    @abstractmethod
    def value(self) -> str:
        """Get the string value for this attribute."""

    def encode(self, quote: str = '"') -> str:
        """Convert this attribute to a string."""

        return f"{self.key}={quote}{self.value}{quote}"

    @staticmethod
    @abstractmethod
    def decode(key: str, value: str) -> "Attribute":
        """Create this attribute from a string."""


class SimpleAttribute(Attribute):
    """A simple, concrete implementation for attribute."""

    def __init__(self, name: str, value: str) -> None:
        """
        Construct a simple attribute, one with just a key (name) and value.
        """

        self.name = name
        self._value = value

    @property
    def value(self) -> str:
        """Get the string value for this attribute."""

        return self._value

    @staticmethod
    def decode(key: str, value: str) -> Attribute:
        """Create this attribute from a string."""

        return SimpleAttribute(key, value)


XMLNS = SimpleAttribute("xmlns", "http://www.w3.org/2000/svg")
