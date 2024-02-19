"""
A module for html-related elements.
"""

# third-party
from vcorelib import DEFAULT_ENCODING

# internal
from svgen.attribute import attributes
from svgen.element import Element

DEFAULT_VIEWPORT = "width=device-width, initial-scale=1"


class Html(Element):
    """A class for html elements."""

    def __init__(
        self,
        title: str,
        viewport: str = DEFAULT_VIEWPORT,
        charset: str = DEFAULT_ENCODING,
        lang: str = "en",
    ) -> None:
        """Initialize this instance."""

        self.head = Element(
            tag="head",
            children=[
                Element(tag="meta", attrib=attributes({"charset": charset})),
                Element(
                    tag="meta",
                    attrib=attributes(
                        {"name": "viewport", "content": viewport}
                    ),
                ),
                Element(tag="title", text=title),
            ],
        )

        self.body = Element(tag="body")

        super().__init__(
            attrib=attributes({"lang": lang}), children=[self.head, self.body]
        )
