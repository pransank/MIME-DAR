"""
Compute word frequency counts from a block of text.
"""

from collections import Counter
from typing import Dict


def word_frequencies(text: str) -> Dict[str, int]:
    """
    Count the frequency of each word in the given text.

    Args:
        text: The input text.

    Returns:
        A dictionary mapping words to their frequency counts.
    """
    words = text.lower().split()
    cleaned_words = [word.strip(".,!?;:\"'") for word in words]
    return dict(Counter(cleaned_words))


if __name__ == "__main__":
    sample = "the quick brown fox jumps over the lazy dog the fox runs"
    print(word_frequencies(sample))
