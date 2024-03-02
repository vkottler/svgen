"""
svgen - A module for XML-style attribute interfaces.
"""

# built-in
from abc import ABC, abstractmethod
from typing import Dict, List, Type, TypeVar, Union

T = TypeVar("T", bound="Attribute")


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
            return str(getattr(self, "name"))

        key = type(self).__name__
        return key[0].lower() + key[1:]

    @property
    @abstractmethod
    def value(self) -> str:
        """Get the string value for this attribute."""

    def encode(self, quote: str = '"', force: bool = False) -> str:
        """Convert this attribute to a string."""

        result = ""
        val = self.value
        if val or force:
            result = f"{self.key}={quote}{val}{quote}"
        return result

    @classmethod
    @abstractmethod
    def decode(cls: Type[T], key: str, value: str) -> T:
        """Create this attribute from a string."""


AttributeValue = Union[str, int, float, bool]


class SimpleAttribute(Attribute):
    """A simple, concrete implementation for attribute."""

    def __init__(self, name: str, value: AttributeValue) -> None:
        """
        Construct a simple attribute, one with just a key (name) and value.
        """

        self.name = name
        self._value = str(value)

    @property
    def value(self) -> str:
        """Get the string value for this attribute."""
        return self._value

    @classmethod
    def decode(
        cls: Type["SimpleAttribute"], key: str, value: str
    ) -> "SimpleAttribute":
        """Create this attribute from a string."""
        return cls(key, value)

    @staticmethod
    def from_dict(data: Dict[str, Union[str, int, float]]) -> List[Attribute]:
        """Get a list of attributes from dictionary data."""
        return [
            SimpleAttribute(key, str(value)) for key, value in data.items()
        ]


PossibleAttributes = Union[
    Dict[str, AttributeValue], List[Attribute], Attribute
]


def attributes(data: PossibleAttributes = None) -> List[Attribute]:
    """
    Get attributes from either an existing list of attributes, or dictionary
    data.
    """

    if data is None:
        data = []
    if isinstance(data, dict):
        data = SimpleAttribute.from_dict(data)
    elif not isinstance(data, list):
        data = [data]
    return data


XMLNS = SimpleAttribute("xmlns", "http://www.w3.org/2000/svg")
