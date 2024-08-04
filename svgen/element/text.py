"""
A module for the 'text' element.
"""

# internal
from svgen.attribute import PossibleAttributes, SimpleAttribute, attributes
from svgen.element.mixins import FillColorMixin, RectangularMixin
from svgen.element.rect import Rect


class Text(FillColorMixin, RectangularMixin):
    """A class for text elements"""

    has_dimensions = False

    def __init__(
        self,
        text: str,
        rect: Rect,
        attrs: PossibleAttributes = None,
        **extra,
    ) -> None:
        """Initialize this instance."""

        RectangularMixin.__init__(self, rect.rect)

        attrib = attributes(attrs) + list(self.rect_attributes)
        attrib += [
            # When would height be used?
            SimpleAttribute("textLength", str(self.dimensions.width / 2)),
            SimpleAttribute("dy", str(self.dimensions.height)),
        ]

        super().__init__(text=text, attrib=attrib, **extra)

        # Get a contrasting text color.
        if rect.has_fill_color:
            self.assign_fill_color(
                rect.fill_color.hsl_arc(lightness_divisor=2)
            )
