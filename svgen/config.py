"""
svgen - A class for managing command-line configuration data.
"""

# built-in
from collections import UserDict


class Config(UserDict):
    """A dictionary that allows access to data only once via each key."""

    def __getitem__(self, path):
        """Consume keys after their data is retreived."""
        result = self.data[path]
        del self.data[path]
        return result

    def set_if_not(self, key, value):
        """Set this value if a value is not already set."""
        if key not in self.data:
            self.data[key] = value
