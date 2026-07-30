"""
A simple queue data structure implementation.
"""

from collections import deque
from typing import Any


class Queue:
    """A first-in-first-out (FIFO) queue."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self) -> Any:
        """Remove and return the item at the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0


if __name__ == "__main__":
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    print(q.dequeue())
