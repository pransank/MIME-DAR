"""
A simple singly linked list implementation.
"""

from typing import Any, Optional


class Node:
    """A single node in a linked list."""

    def __init__(self, value: Any):
        self.value = value
        self.next: Optional["Node"] = None


class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, value: Any) -> None:
        """Append a value to the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def to_list(self) -> list:
        """Convert the linked list into a Python list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result


if __name__ == "__main__":
    ll = LinkedList()
    for item in [1, 2, 3]:
        ll.append(item)
    print(ll.to_list())
