"""
svgen - A module for converting colors from some form to some other.
"""

# built-in
from math import isclose

# internal
from svgen.color.hsl import Hsl, hsla
from svgen.color.rgb import Rgb, rgba


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

    return rgba(
        round((red + common) * 255.0),
        round((green + common) * 255.0),
        round((blue + common) * 255.0),
        float(color.alpha),
    )


def rgb_to_hsl(color: Rgb) -> Hsl:
    """Convert an rgb color to an hsl color."""

    red = color.red.ratio
    green = color.green.ratio
    blue = color.blue.ratio

    cmax = max(red, green, blue)
    cmin = min(red, green, blue)
    delta = cmax - cmin

    hue = 0.0
    if not isclose(delta, 0.0):
        if cmax == red:
            hue = 60.0 * (((green - blue) / delta) % 6.0)
        elif cmax == green:
            hue = 60.0 * ((blue - red) / delta + 2.0)
        else:
            hue = 60.0 * ((red - green) / delta + 4.0)

    light = (cmax + cmin) / 2.0

    saturation = 0.0
    if not isclose(delta, 0.0):
        saturation = delta / (1.0 - abs(2.0 * light - 1.0))

    return hsla(round(hue), saturation, light, float(color.alpha))
