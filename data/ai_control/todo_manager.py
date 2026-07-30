"""
A simple in-memory to-do list manager.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    """A single to-do item."""

    description: str
    completed: bool = False


@dataclass
class TodoManager:
    """Manages a collection of to-do tasks."""

    tasks: List[Task] = field(default_factory=list)

    def add_task(self, description: str) -> None:
        """Add a new task."""
        self.tasks.append(Task(description=description))

    def complete_task(self, index: int) -> None:
        """Mark a task as completed by its index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def pending_tasks(self) -> List[Task]:
        """Return all tasks that are not yet completed."""
        return [task for task in self.tasks if not task.completed]


if __name__ == "__main__":
    manager = TodoManager()
    manager.add_task("Write research paper")
    manager.add_task("Collect dataset")
    manager.complete_task(0)
    print(manager.pending_tasks())
