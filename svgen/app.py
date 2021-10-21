"""
svgen - This package's command-line entry-point application.
"""

# built-in
import argparse


def entry(args: argparse.Namespace) -> int:
    """Execute the requested task."""

    print(args)
    return 0


def add_app_args(_: argparse.ArgumentParser) -> None:
    """Add application-specific arguments to the command-line parser."""
