# =====================================
# generator=datazen
# version=1.9.4
# hash=a2daeab9d81c0c89ff1f3b5f9397dcc7
# =====================================

"""
svgen - Package definition for distribution.
"""

# third-party
try:
    from vmklib.setup import setup
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
    ],
}
setup(
    pkg_info,
    author_info,
    entry_override="svgen",
)
