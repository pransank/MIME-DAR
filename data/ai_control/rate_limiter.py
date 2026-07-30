"""
A simple in-memory rate limiter using a sliding window.
"""

import time
from collections import deque
from typing import Deque


class RateLimiter:
    """Limits the number of allowed actions within a time window."""

    def __init__(self, max_calls: int, window_seconds: float):
        self.max_calls = max_calls
        self.window_seconds = window_seconds
        self._timestamps: Deque[float] = deque()

    def allow(self) -> bool:
        """
        Check whether a new action is allowed under the rate limit.

        Returns:
            True if the action is allowed, False otherwise.
        """
        now = time.time()
        while self._timestamps and now - self._timestamps[0] > self.window_seconds:
            self._timestamps.popleft()

        if len(self._timestamps) < self.max_calls:
            self._timestamps.append(now)
            return True

        return False


if __name__ == "__main__":
    limiter = RateLimiter(max_calls=3, window_seconds=5)
    print(limiter.allow())
