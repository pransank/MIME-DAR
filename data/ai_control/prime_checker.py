"""
Utility functions for checking prime numbers.
"""

import math


def is_prime(number: int) -> bool:
    """
    Determine whether a number is prime.

    Args:
        number: The integer to test.

    Returns:
        True if the number is prime, False otherwise.
    """
    if number < 2:
        return False

    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False

    return True


def primes_up_to(limit: int) -> list:
    """
    Return a list of all prime numbers up to a given limit.

    Args:
        limit: The upper bound (inclusive).

    Returns:
        A list of prime numbers.
    """
    return [n for n in range(2, limit + 1) if is_prime(n)]


if __name__ == "__main__":
    print(primes_up_to(50))
