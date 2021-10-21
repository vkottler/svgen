"""
svgen - Test the program's entry-point.
"""

# module under test
from svgen import PKG_NAME
from svgen.entry import main as svgen_main


def test_entry_basic():
    """Test basic argument parsing."""

    args = [PKG_NAME]
    assert svgen_main(args) == 0
