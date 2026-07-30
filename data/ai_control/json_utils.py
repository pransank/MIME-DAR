"""
Utility functions for reading and writing JSON files.
"""

import json
from typing import Any


def load_json(filepath: str) -> Any:
    """Load and parse a JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: Any, filepath: str) -> None:
    """Write data to a JSON file with indentation."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    pass
