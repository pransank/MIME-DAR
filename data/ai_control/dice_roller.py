"""
A simple dice rolling simulator.
"""

import random
from typing import List


def roll_dice(num_dice: int = 1, sides: int = 6) -> List[int]:
    """
    Roll a number of dice with a given number of sides.

    Args:
        num_dice: The number of dice to roll.
        sides: The number of sides per die.

    Returns:
        A list of individual die results.
    """
    return [random.randint(1, sides) for _ in range(num_dice)]


def roll_total(num_dice: int = 1, sides: int = 6) -> int:
    """Return the sum of a dice roll."""
    return sum(roll_dice(num_dice, sides))


if __name__ == "__main__":
    print(roll_dice(2, 6))
    print(roll_total(2, 6))
