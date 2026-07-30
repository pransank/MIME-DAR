"""
Breadth-first search implementation for a graph represented as an
adjacency list.
"""

from collections import deque
from typing import Dict, List


def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    Perform a breadth-first traversal of a graph.

    Args:
        graph: An adjacency list mapping nodes to their neighbors.
        start: The starting node.

    Returns:
        A list of nodes in the order they were visited.
    """
    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    sample_graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }
    print(bfs(sample_graph, "A"))
