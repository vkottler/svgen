"""
svgen - Common interfaces and assets for SVG elements.
"""

# built-in
from io import StringIO
import os
from typing import Dict, List

# internal
from svgen.attribute import Attribute

INDENT: int = 2


class Element:
    """A basic interface for an SVG element."""

    def __init__(
        self,
        name: str = None,
        content: str = "",
        attributes: List[Attribute] = None,
        children: List["Element"] = None,
    ) -> None:
        """Construct a new SVG element."""

        if name is None:
            name = type(self).__name__
            name = name[0].lower() + name[1:]
        if attributes is None:
            attributes = []
        if children is None:
            children = []

        self.name = name
        self.content = content

        self.attributes: Dict[str, Attribute] = {}
        for attr in attributes:
            self.attributes[attr.key] = attr

        self.children: List[Element] = children

    def closing(self, indent: int = 0) -> str:
        """Create a string to close this element."""

        if not self.content and not self.children:
            return " />"

        indent_str = " " * (indent * INDENT)
        return f"{indent_str}</{self.name}>"

    def encode(
        self,
        output: StringIO,
        quote: str = '"',
        indent: int = 0,
        newlines: bool = True,
    ) -> None:
        """Encode this element to a string stream."""

        # Indent will matter if we want lines.
        indent_str = " " * (indent * INDENT)
        if newlines:
            output.write(indent_str)

        attrs = " ".join(x.encode(quote) for x in self.attributes.values())
        output.write(f"<{self.name}")
        if attrs:
            output.write(f" {attrs}")

        if self.content or self.children:
            # Close the opening tag.
            output.write(">")
            if newlines:
                output.write(os.linesep)

            # Write content, if any.
            if newlines:
                output.write(indent_str + " " * INDENT)
            output.write(self.content)
            if newlines:
                output.write(os.linesep)

            # Write children.
            for child in self.children:
                child.encode(output, quote, indent + 1, newlines)

        # Close this element tag.
        output.write(self.closing(indent))
        if newlines:
            output.write(os.linesep)

    def encode_str(
        self,
        quote: str = '"',
        indent: int = 0,
        newlines: bool = True,
    ) -> str:
        """Encode this element to a string."""

        output = StringIO()
        self.encode(output, quote, indent, newlines)
        return output.getvalue()
