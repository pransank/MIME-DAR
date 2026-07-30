"""
A decorator for retrying a function call on failure.
"""

import functools
import time
from typing import Callable


def retry(max_attempts: int = 3, delay_seconds: float = 1.0) -> Callable:
    """
    Create a decorator that retries a function on exception.

    Args:
        max_attempts: The maximum number of attempts before giving up.
        delay_seconds: The delay between retry attempts.

    Returns:
        A decorator function.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exception = exc
                    if attempt < max_attempts:
                        time.sleep(delay_seconds)
            raise last_exception

        return wrapper

    return decorator


if __name__ == "__main__":
    @retry(max_attempts=2, delay_seconds=0.1)
    def flaky_function():
        raise ValueError("Simulated failure")

    try:
        flaky_function()
    except ValueError:
        print("Failed after retries")
