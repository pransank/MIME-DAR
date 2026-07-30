"""
Simple email address validation utility.
"""

import re

EMAIL_PATTERN = re.compile(r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$")


def is_valid_email(email: str) -> bool:
    """
    Check whether a string is a syntactically valid email address.

    Args:
        email: The email address to validate.

    Returns:
        True if the email address matches the expected pattern.
    """
    return bool(EMAIL_PATTERN.match(email))


if __name__ == "__main__":
    print(is_valid_email("test@example.com"))
    print(is_valid_email("not-an-email"))
