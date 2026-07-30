"""
Utility functions for hashing strings and files.
"""

import hashlib


def hash_string(text: str, algorithm: str = "sha256") -> str:
    """
    Compute the hash of a string using the specified algorithm.

    Args:
        text: The input string.
        algorithm: The hashing algorithm to use.

    Returns:
        The hexadecimal digest of the hash.
    """
    hasher = hashlib.new(algorithm)
    hasher.update(text.encode("utf-8"))
    return hasher.hexdigest()


def hash_file(filepath: str, algorithm: str = "sha256") -> str:
    """
    Compute the hash of a file's contents.

    Args:
        filepath: Path to the file.
        algorithm: The hashing algorithm to use.

    Returns:
        The hexadecimal digest of the hash.
    """
    hasher = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


if __name__ == "__main__":
    print(hash_string("hello world"))
