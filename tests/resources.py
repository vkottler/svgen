"""
svgen - An interface for retrieving and interacting with test data.
"""

# built-in
from contextlib import contextmanager
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator, List

# third-party
import pkg_resources

# internal
from svgen import PKG_NAME


def get_resource(resource_name: str, *names: str, pkg: str = __name__) -> Path:
    """Locate the path to a test resource."""

    resource_path = os.path.join("data", resource_name, *names)
    return Path(pkg_resources.resource_filename(pkg, resource_path))


def get_config(name: str = "sample") -> Path:
    """Get the path to a test configuration."""
    return get_resource(f"{name}.json")


def get_script(name: str = "sample") -> Path:
    """Get the path to a test script."""
    return get_resource(f"{name}.py")


@contextmanager
def base_args(
    name: str = "sample", include_config: bool = True
) -> Iterator[List[str]]:
    """Get base arguments to invoke this package's command-line entry."""

    with TemporaryDirectory() as tmpdir:
        args = [PKG_NAME, "-C", tmpdir, "--images"]
        if include_config:
            args.extend(["-c", str(get_config(name))])
        args.append(str(get_script(name)))
        yield args
