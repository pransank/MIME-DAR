"""
Implementation of the bubble sort algorithm.
"""

from typing import List


def bubble_sort(values: List[int]) -> List[int]:
    """
    Sort a list of integers using bubble sort.

    Args:
        values: The list of integers to sort.

    Returns:
        A new sorted list.
    """
    result = values.copy()
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1, 5, 6]))
