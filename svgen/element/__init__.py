"""
svgen - Common interfaces and assets for SVG elements.
"""

# built-in
from io import StringIO
import os
from typing import Dict, List, TextIO, cast
from xml.etree import ElementTree as et

# internal
from svgen.attribute import (
    Attribute,
    AttributeValue,
    SimpleAttribute,
    attributes,
)
from svgen.attribute.style import Style

INDENT: int = 2


class Element:
    """A basic interface for an SVG element."""

    def __init__(
        self,
        tag: str = None,
        text: str = "",
        attrib: List[Attribute] = None,
        children: List["Element"] = None,
        **extra,
    ) -> None:
        """Construct a new SVG element."""

        if tag is None:
            tag = type(self).__name__
            tag = tag[0].lower() + tag[1:]
        if attrib is None:
            attrib = []
        if children is None:
            children = []

        self.tag = tag
        self.text = text

        self.attributes: Dict[str, Attribute] = {}
        for attr in attrib + attributes(extra):
            self.add_attribute(attr)

        self.children: List[Element] = children

    def __setitem__(self, tag: str, value: AttributeValue) -> None:
        """Allow adding attributes dict-set style."""
        self.add_attribute(SimpleAttribute(tag, value))

    @property
    def xml(self) -> et.Element:
        """Get this element as an xml element."""

        elem = et.Element(
            self.tag, {x.key: x.value for x in self.attributes.values()}
        )
        elem.text = self.text

        # Add children.
        elem.extend(child.xml for child in self.children)
        return elem

    @property
    def style(self) -> Style:
        """Get the style attribute for this element."""

        if "style" not in self.attributes:
            self.add_attribute(Style())
        return cast(Style, self.attributes["style"])

    def add_attribute(self, attr: Attribute) -> "Element":
        """Add an attribute to this element."""
        assert (
            attr.key not in self.attributes
        ), f"This '{self.tag}' element already has attribute '{attr.key}'!"
        self.attributes[attr.key] = attr
        return self

    def closing(self, indent: int = 0) -> str:
        """Create a string to close this element."""

        if not self.text and not self.children:
            return " />"

        indent_str = " " * (indent * INDENT)
        return f"{indent_str}</{self.tag}>"

    def _write_text(
        self, output: TextIO, indent_str: str, newlines: bool = True
    ) -> None:
        """Write the inner-text section of this element."""

        if not newlines:
            output.write(self.text)
            return

        # Increase indent one level.
        indent_str += " " * INDENT
        for line in self.text.splitlines():
            output.write(indent_str + line)
            output.write(os.linesep)

    def encode(
        self,
        output: TextIO,
        quote: str = '"',
        indent: int = 0,
        newlines: bool = True,
    ) -> None:
        """Encode this element to a string stream."""

        # Indent will matter if we want lines.
        indent_str = " " * (indent * INDENT)
        if newlines:
            output.write(indent_str)

        attr_strs = [x.encode(quote) for x in self.attributes.values()]
        attrs = " ".join(x for x in attr_strs if x)
        output.write(f"<{self.tag}")
        if attrs:
            output.write(f" {attrs}")

        if self.text or self.children:
            # Close the opening tag.
            output.write(">")
            if newlines:
                output.write(os.linesep)

            # Write content, if any.
            if self.text:
                self._write_text(output, indent_str, newlines=newlines)

            # Write children.
            for child in self.children:
                if child:
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

        with StringIO() as output:
            self.encode(output, quote, indent, newlines)
            return output.getvalue()
