"""
Statistical utilities for analyzing a series of temperature readings.
"""

from typing import List


def mean(values: List[float]) -> float:
    """Compute the arithmetic mean of a list of numbers."""
    return sum(values) / len(values)


def variance(values: List[float]) -> float:
    """Compute the population variance of a list of numbers."""
    avg = mean(values)
    return sum((x - avg) ** 2 for x in values) / len(values)


def standard_deviation(values: List[float]) -> float:
    """Compute the population standard deviation of a list of numbers."""
    return variance(values) ** 0.5


if __name__ == "__main__":
    readings = [72.1, 75.3, 68.9, 71.0, 74.2]
    print(mean(readings))
    print(standard_deviation(readings))
