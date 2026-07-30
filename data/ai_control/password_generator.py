"""
A random password generator.
"""

import random
import string


def generate_password(length: int = 12, include_symbols: bool = True) -> str:
    """
    Generate a random password.

    Args:
        length: The desired password length.
        include_symbols: Whether to include special characters.

    Returns:
        A randomly generated password string.
    """
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    print(generate_password(16))
