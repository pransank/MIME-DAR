"""
Module for computing Fibonacci sequence values.
"""


def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number using iteration.

    Args:
        n: The index of the Fibonacci number to compute.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current


def fibonacci_sequence(count: int) -> list:
    """
    Generate a list of the first `count` Fibonacci numbers.

    Args:
        count: The number of Fibonacci numbers to generate.

    Returns:
        A list containing the Fibonacci sequence.
    """
    return [fibonacci(i) for i in range(count)]


if __name__ == "__main__":
    print(fibonacci_sequence(10))
