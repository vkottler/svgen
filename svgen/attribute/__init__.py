"""
svgen - A module for XML-style attribute interfaces.
"""

# built-in
from abc import ABC, abstractmethod


class Attribute(ABC):
    """An interface for an XML-style attribute."""

    @property
    @abstractmethod
    def key(self) -> str:
        """Get the string key for this attribute."""

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
