"""
svgen - Test the program's entry-point.
"""

# built-in
from unittest.mock import patch

# module under test
from svgen.entry import main as svgen_main

# internal
from tests.resources import base_args


def test_entry_basic():
    """Test basic argument parsing."""

    with base_args() as args:
        assert svgen_main(args) == 0

        with patch("svgen.entry.entry", side_effect=SystemExit(1)):
            assert svgen_main(args) != 0

    with base_args(include_config=False) as args:
        assert svgen_main(args) == 0
