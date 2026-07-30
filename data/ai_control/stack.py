"""
A simple stack data structure implementation.
"""

from typing import Any, List


class Stack:
    """A last-in-first-out (LIFO) stack."""

    def __init__(self):
        self._items: List[Any] = []

    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the top item of the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())
