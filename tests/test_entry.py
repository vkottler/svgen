"""
svgen - Test the program's entry-point.
"""

# built-in
from asyncio import run
from contextlib import suppress
from subprocess import check_output
from sys import executable
from typing import Coroutine
from unittest.mock import patch

# module under test
from svgen import PKG_NAME
from svgen.entry import main as svgen_main

# internal
from tests.resources import base_args


def test_entry_basic():
    """Test basic argument parsing."""

    with base_args() as args:
        with patch("svgen.entry.entry", side_effect=SystemExit(1)):
            assert svgen_main(args) != 0

    with base_args(include_config=False) as args:
        assert svgen_main(args) == 0


def test_entry_bypass_generation():
    """
    Test image generation logic even if 'inkscape' is not found on the system.
    """

    def run_patch(awaitable: Coroutine) -> bool:
        """Run the coroutine but always return True."""
        with suppress(FileNotFoundError):
            run(awaitable)
        return True

    # Patch 'asyncio.run' so that icon generation runs.
    with patch("svgen.generation.images.run", new=run_patch):
        with base_args() as args:
            assert svgen_main(args) == 0


def test_package_entry():
    """Test the command-line entry through the 'python -m' invocation."""

    check_output([executable, "-m", PKG_NAME, "-h"])
