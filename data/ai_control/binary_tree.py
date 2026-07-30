"""
A basic binary search tree implementation.
"""

from typing import Any, Optional


class TreeNode:
    """A node in a binary search tree."""

    def __init__(self, value: Any):
        self.value = value
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class BinarySearchTree:
    """A binary search tree supporting insertion and in-order traversal."""

    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, value: Any) -> None:
        """Insert a value into the tree."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: Any) -> None:
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order(self) -> list:
        """Return the values of the tree in sorted order."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node: Optional[TreeNode], result: list) -> None:
        if node is not None:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for value in [5, 3, 8, 1, 4]:
        bst.insert(value)
    print(bst.in_order())
