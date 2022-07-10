"""
svgen - A module for working with external scripts.
"""

# built-in
from pathlib import Path

# third-party
from vcorelib.dict.config import Config
from vcorelib.script import invoke_script as script

# internal
from svgen.element.svg import Svg


def invoke_script(path: Path, svg: Svg, config: Config) -> None:
    """Invoke an external script's 'compose' function."""

    # Compose the document.
    svg.children.extend(script(path, "compose", svg.viewbox, config))
