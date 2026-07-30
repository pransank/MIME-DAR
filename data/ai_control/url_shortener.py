"""
A simple in-memory URL shortener.
"""

import hashlib
from typing import Dict


class URLShortener:
    """Maps long URLs to short hashed codes."""

    def __init__(self):
        self._mapping: Dict[str, str] = {}

    def shorten(self, long_url: str) -> str:
        """
        Generate a short code for a given URL.

        Args:
            long_url: The original URL.

        Returns:
            A short code representing the URL.
        """
        short_code = hashlib.md5(long_url.encode("utf-8")).hexdigest()[:8]
        self._mapping[short_code] = long_url
        return short_code

    def resolve(self, short_code: str) -> str:
        """
        Resolve a short code back to its original URL.

        Args:
            short_code: The short code to resolve.

        Returns:
            The original URL, or an empty string if not found.
        """
        return self._mapping.get(short_code, "")


if __name__ == "__main__":
    shortener = URLShortener()
    code = shortener.shorten("https://www.example.com/some/long/path")
    print(code, shortener.resolve(code))
