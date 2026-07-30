"""
Utility for reading and summarizing CSV files.
"""

import csv
from typing import Dict, List


def read_csv(filepath: str) -> List[Dict[str, str]]:
    """
    Read a CSV file into a list of dictionaries.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A list of rows represented as dictionaries.
    """
    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def column_values(rows: List[Dict[str, str]], column: str) -> List[str]:
    """Extract all values for a given column from parsed CSV rows."""
    return [row[column] for row in rows if column in row]


if __name__ == "__main__":
    pass
