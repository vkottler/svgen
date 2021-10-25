"""
svgen - A module for converting colors from some form to some other.
"""

# internal
from svgen.color.hsl import Hsl
from svgen.color.rgb import Rgb, rgb


def hsl_to_rgb(color: Hsl) -> Rgb:
    """Convert an hsl color to rgb."""

    hue = color.hue
    sat = color.saturation.ratio
    light = color.lightness.ratio

    # pylint: disable=invalid-name
    c = (1.0 - abs(2.0 * light - 1.0)) * sat
    x = c * (1.0 - abs(float(hue) / 60.0 % 2.0 - 1.0))
    common = light - c / 2.0

    red = 0.0
    blue = 0.0
    green = 0.0
    if 0 <= hue < 60:
        red = c
        green = x
    elif 60 <= hue < 120:
        red = x
        green = c
    elif 120 <= hue < 180:
        green = c
        blue = x
    elif 180 <= hue < 240:
        green = x
        blue = c
    elif 240 <= hue < 300:
        red = x
        blue = c
    elif 300 <= hue < 360:
        red = c
        blue = x
    # pylint: enable=invalid-name

    return rgb(
        round((red + common) * 255.0),
        round((green + common) * 255.0),
        round((blue + common) * 255.0),
    )
