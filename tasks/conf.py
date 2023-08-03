# =====================================
# generator=datazen
# version=3.1.2
# hash=9f62028523c3b5a953733ca89dcc3018
# =====================================
"""
A module for project-specific task registration.
"""

# built-in
from pathlib import Path
from subprocess import run
from typing import Dict

# third-party
from vcorelib.task.manager import TaskManager


def audit_local_tasks() -> None:
    """Ensure that shared task infrastructure is present."""

    local = Path(__file__).parent.joinpath("mklocal")

    # Also link a top-level file.
    top_level = local.parent.parent.joinpath("mklocal")
    if not top_level.is_symlink():
        assert not top_level.exists()
        top_level.symlink_to(local)

    if local.is_symlink():
        return

    # If it's not a symlink, it shouldn't be any other kind of file.
    assert not local.exists()

    # Ensure sub-module implementation is present.
    config = local.parent.parent.joinpath("config")
    assert config.is_dir()

    # Initialize submodules if we don't see the directory we're looking for.
    vmklib = config.joinpath("python", "mklocal")
    if not vmklib.is_dir():
        run(
            ["git", "-C", str(config.parent), "submodule", "update", "--init"],
            check=True,
        )

    # Create the link.
    local.symlink_to(vmklib)


def register(
    manager: TaskManager,
    project: str,
    cwd: Path,
    substitutions: Dict[str, str],
) -> bool:
    """Register project tasks to the manager."""

    audit_local_tasks()

    from mklocal.python import (  # pylint: disable=import-outside-toplevel
        register_python,
    )

    return register_python(manager, project, cwd, substitutions)
