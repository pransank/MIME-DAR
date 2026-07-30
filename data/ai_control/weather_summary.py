"""
Summarize a list of daily weather readings.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class DailyReading:
    """A single day's weather reading."""

    day: str
    high_temp: float
    low_temp: float
    precipitation_mm: float


def average_high(readings: List[DailyReading]) -> float:
    """Compute the average high temperature across readings."""
    return sum(r.high_temp for r in readings) / len(readings)


def rainiest_day(readings: List[DailyReading]) -> DailyReading:
    """Return the reading with the highest precipitation."""
    return max(readings, key=lambda r: r.precipitation_mm)


if __name__ == "__main__":
    data = [
        DailyReading("Mon", 75.0, 60.0, 0.0),
        DailyReading("Tue", 70.0, 58.0, 12.5),
        DailyReading("Wed", 68.0, 55.0, 3.2),
    ]
    print(average_high(data))
    print(rainiest_day(data).day)
