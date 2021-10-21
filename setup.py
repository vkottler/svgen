# =====================================
# generator=datazen
# version=1.8.4
# hash=bde9e276cefb35a79064f9876f4b239d
# =====================================

"""
svgen - Package definition for distribution.
"""

# third-party
from vmklib.setup import setup

# internal
from svgen import PKG_NAME, VERSION, DESCRIPTION


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
        "3.6",
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
