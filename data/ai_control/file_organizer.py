"""
Utility for organizing files in a directory by extension.
"""

import os
import shutil
from pathlib import Path


def organize_by_extension(directory: str) -> None:
    """
    Move files in the given directory into subfolders named
    after their file extensions.

    Args:
        directory: Path to the directory to organize.
    """
    directory_path = Path(directory)

    for item in directory_path.iterdir():
        if item.is_file():
            extension = item.suffix.lstrip(".").lower() or "no_extension"
            target_folder = directory_path / extension
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_folder / item.name))


if __name__ == "__main__":
    organize_by_extension(".")
