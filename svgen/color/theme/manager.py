"""
A module implementing a color-theme manager.
"""

# built-in
from collections import UserDict
from typing import Dict

# third-party
from vcorelib.logging import LoggerMixin
from vcorelib.paths import Pathlike, normalize

# internal
from svgen.color import Colorlike
from svgen.color.theme import ColorTheme, ColorToken


class ColorThemeManager(UserDict, LoggerMixin):
    """A class for managing color themes."""

    def __init__(
        self, initialdata: Dict[str, ColorTheme] = None, theme: str = ""
    ) -> None:
        """Initialize this theme manager."""

        UserDict.__init__(self, initialdata=initialdata)
        LoggerMixin.__init__(self)
        self.theme: str = theme

    def __getitem__(self, key: Colorlike) -> ColorToken:
        """Attempt to get a color token based on a color key."""
        if self.theme and self.theme in self.data:
            return self.data[self.theme].create(key)
        return ColorToken.create(key)

    @property
    def size(self) -> int:
        """Get the number of managed themes."""
        return len(self.data.keys())

    def add_themes(self, *themes: ColorTheme) -> None:
        """Add new themes to the manager."""
        for theme in [*themes]:
            assert (
                theme.name not in self.data
            ), f"Duplicate theme '{theme.name}'!"

            self.data[theme.name] = theme
            self.logger.info(
                "Added theme '%s' with %d colors.", theme.name, theme.size
            )

    def load_directory(self, path: Pathlike) -> None:
        """Load themes from a directory."""

        path = normalize(path)
        assert path.is_dir(), f"'{path}' is not a directory!"
        self.add_themes(
            *[ColorTheme.from_path(x) for x in path.iterdir() if x.is_file()]
        )


THEMES = ColorThemeManager()
