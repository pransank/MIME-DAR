"""
Implementation of the binary search algorithm.
"""

from typing import List, Optional


def binary_search(sorted_list: List[int], target: int) -> Optional[int]:
    """
    Perform a binary search on a sorted list.

    Args:
        sorted_list: A list of integers sorted in ascending order.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise None.
    """
    low, high = 0, len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(data, 7))
