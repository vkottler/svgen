"""
svgen - A module for working with external scripts.
"""

# built-in
import importlib.machinery
import importlib.util
from pathlib import Path

# internal
from svgen.config import Config
from svgen.element.svg import Svg


def invoke_script(script: Path, svg: Svg, config: Config) -> None:
    """Invoke an external script's 'compose' function."""

    loader = importlib.machinery.SourceFileLoader("script", str(script))
    spec = importlib.util.spec_from_loader("script", loader)
    assert spec is not None
    script_module = importlib.util.module_from_spec(spec)
    loader.exec_module(script_module)

    # Compose the document.
    svg.children.extend(script_module.compose(svg.viewbox, config))
