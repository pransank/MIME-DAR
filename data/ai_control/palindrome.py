"""
Utility function to check whether a string is a palindrome.
"""

import re


def is_palindrome(text: str) -> bool:
    """
    Determine whether the given text is a palindrome.

    Args:
        text: The input string.

    Returns:
        True if the text is a palindrome, ignoring case and
        non-alphanumeric characters.
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))
