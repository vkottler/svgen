# =====================================
# generator=datazen
# version=3.0.8
# hash=a8a0d03626a8371219b90fe5e4a7a49a
# =====================================

"""
svgen - Package definition for distribution.
"""

# third-party
try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from svgen_bootstrap.setup import setup  # type: ignore

# internal
from svgen import DESCRIPTION, PKG_NAME, VERSION

author_info = {
    "name": "Vaughn Kottler",
    "email": "vaughnkottler@gmail.com",
    "username": "vkottler",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.7",
        "3.8",
        "3.9",
        "3.10",
    ],
}
setup(
    pkg_info,
    author_info,
)
