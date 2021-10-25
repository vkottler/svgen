"""
svgen - Test the 'svgen.color.conversion' module.
"""

# module under test
from svgen.color.conversion import hsl_to_rgb
from svgen.color.hsl import hsl, Hsl
from svgen.color.rgb import rgb, Rgb


def test_hsl_to_rgb_basic():
    """TODO."""

    color = rgb(255, 0, 0)
    assert hsl_to_rgb(hsl(0, 1.0, 0.5)) == color

    assert hsl_to_rgb(hsl(0, 0.0, 0.0)) == rgb(0, 0, 0)
    assert hsl_to_rgb(hsl(0, 0.0, 1.0)) == rgb(255, 255, 255)
    assert hsl_to_rgb(hsl(120, 1.0, 0.5)) == rgb(0, 255, 0)

    # Black.
    assert hsl_to_rgb(Hsl.from_ctor("0, 0%, 0%")) == Rgb.from_ctor("0, 0, 0")

    # White.
    assert hsl_to_rgb(Hsl.from_ctor("0, 0%, 100%")) == Rgb.from_ctor(
        "255, 255, 255"
    )

    # Red.
    assert hsl_to_rgb(Hsl.from_ctor("0, 100%, 50%")) == Rgb.from_ctor(
        "255, 0, 0"
    )

    # Lime.
    assert hsl_to_rgb(Hsl.from_ctor("120, 100%, 50%")) == Rgb.from_ctor(
        "0, 255, 0"
    )

    # Blue.
    assert hsl_to_rgb(Hsl.from_ctor("240, 100%, 50%")) == Rgb.from_ctor(
        "0, 0, 255"
    )

    # Yellow.
    assert hsl_to_rgb(Hsl.from_ctor("60, 100%, 50%")) == Rgb.from_ctor(
        "255, 255, 0"
    )

    # Cyan.
    assert hsl_to_rgb(Hsl.from_ctor("180, 100%, 50%")) == Rgb.from_ctor(
        "0, 255, 255"
    )

    # Magenta.
    assert hsl_to_rgb(Hsl.from_ctor("300, 100%, 50%")) == Rgb.from_ctor(
        "255, 0, 255"
    )

    # Silver.
    assert hsl_to_rgb(Hsl.from_ctor("0, 0%, 75%")) == Rgb.from_ctor(
        "191, 191, 191"
    )

    # Gray.
    assert hsl_to_rgb(Hsl.from_ctor("0, 0%, 50%")) == Rgb.from_ctor(
        "128, 128, 128"
    )

    # Maroon.
    assert hsl_to_rgb(Hsl.from_ctor("0, 100%, 25%")) == Rgb.from_ctor(
        "128, 0, 0"
    )

    # Olive.
    assert hsl_to_rgb(Hsl.from_ctor("60, 100%, 25%")) == Rgb.from_ctor(
        "128, 128, 0"
    )

    # Green.
    assert hsl_to_rgb(Hsl.from_ctor("120, 100%, 25%")) == Rgb.from_ctor(
        "0, 128, 0"
    )

    # Purple.
    assert hsl_to_rgb(Hsl.from_ctor("300, 100%, 25%")) == Rgb.from_ctor(
        "128, 0, 128"
    )

    # Teal.
    assert hsl_to_rgb(Hsl.from_ctor("180, 100%, 25%")) == Rgb.from_ctor(
        "0, 128, 128"
    )

    # Navy.
    assert hsl_to_rgb(Hsl.from_ctor("240, 100%, 25%")) == Rgb.from_ctor(
        "0, 0, 128"
    )

    # Arbitrary.
    assert hsl_to_rgb(Hsl.from_ctor("26, 85%, 64%")) == Rgb.from_ctor(
        "241, 153, 85"
    )
    assert hsl_to_rgb(Hsl.from_ctor("300, 19%, 22%")) == Rgb.from_ctor(
        "67, 45, 67"
    )
