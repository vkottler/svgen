"""
svgen - Test the 'svgen.color.conversion' module.
"""

# module under test
from svgen.color.conversion import hsl_to_rgb, rgb_to_hsl
from svgen.color.hsl import hsl, Hsl
from svgen.color.rgb import rgb, Rgb


def test_hsla_to_rgba_basic():
    """Test that the hsla to rgba conversion works."""

    # Arbitrary.
    assert rgb_to_hsl(Rgb.from_ctor("241, 153, 85, 0.25")) == Hsl.from_ctor(
        "26, 85%, 64%, 0.25"
    )
    assert rgb_to_hsl(Rgb.from_ctor("82, 30, 82")) == Hsl.from_ctor(
        "300, 46%, 22%"
    )


def test_hsl_to_rgb_basic():
    """Test that the hsl to rgb conversion works."""

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


def test_rgb_to_hsl_basic():
    """Test that the rgb to hsl conversion works."""

    # Black.
    assert rgb_to_hsl(Rgb.from_ctor("0, 0, 0")) == Hsl.from_ctor("0, 0%, 0%")

    # White.
    assert rgb_to_hsl(Rgb.from_ctor("255, 255, 255")) == Hsl.from_ctor(
        "0, 0%, 100%"
    )

    # Red.
    assert rgb_to_hsl(Rgb.from_ctor("255, 0, 0")) == Hsl.from_ctor(
        "0, 100%, 50%"
    )

    # Lime.
    assert rgb_to_hsl(Rgb.from_ctor("0, 255, 0")) == Hsl.from_ctor(
        "120, 100%, 50%"
    )

    # Blue.
    assert rgb_to_hsl(Rgb.from_ctor("0, 0, 255")) == Hsl.from_ctor(
        "240, 100%, 50%"
    )

    # Yellow.
    assert rgb_to_hsl(Rgb.from_ctor("255, 255, 0")) == Hsl.from_ctor(
        "60, 100%, 50%"
    )

    # Cyan.
    assert rgb_to_hsl(Rgb.from_ctor("0, 255, 255")) == Hsl.from_ctor(
        "180, 100%, 50%"
    )

    # Magenta.
    assert rgb_to_hsl(Rgb.from_ctor("255, 0, 255")) == Hsl.from_ctor(
        "300, 100%, 50%"
    )

    # Silver.
    assert rgb_to_hsl(Rgb.from_ctor("191, 191, 191")) == Hsl.from_ctor(
        "0, 0%, 75%"
    )

    # Gray.
    assert rgb_to_hsl(Rgb.from_ctor("128, 128, 128")) == Hsl.from_ctor(
        "0, 0%, 50%"
    )

    # Maroon.
    assert rgb_to_hsl(Rgb.from_ctor("128, 0, 0")) == Hsl.from_ctor(
        "0, 100%, 25%"
    )

    # Olive.
    assert rgb_to_hsl(Rgb.from_ctor("128, 128, 0")) == Hsl.from_ctor(
        "60, 100%, 25%"
    )

    # Green.
    assert rgb_to_hsl(Rgb.from_ctor("0, 128, 0")) == Hsl.from_ctor(
        "120, 100%, 25%"
    )

    # Purple.
    assert rgb_to_hsl(Rgb.from_ctor("128, 0, 128")) == Hsl.from_ctor(
        "300, 100%, 25%"
    )

    # Teal.
    assert rgb_to_hsl(Rgb.from_ctor("0, 128, 128")) == Hsl.from_ctor(
        "180, 100%, 25%"
    )

    # Navy.
    assert rgb_to_hsl(Rgb.from_ctor("0, 0, 128")) == Hsl.from_ctor(
        "240, 100%, 25%"
    )

    # Arbitrary.
    assert rgb_to_hsl(Rgb.from_ctor("241, 153, 85")) == Hsl.from_ctor(
        "26, 85%, 64%"
    )
    assert rgb_to_hsl(Rgb.from_ctor("82, 30, 82")) == Hsl.from_ctor(
        "300, 46%, 22%"
    )
