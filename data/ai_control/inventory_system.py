"""
A basic inventory management system.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Item:
    """Represents a single inventory item."""

    name: str
    quantity: int
    unit_price: float

    def total_value(self) -> float:
        """Return the total value of this item's stock."""
        return self.quantity * self.unit_price


class Inventory:
    """Manages a collection of inventory items."""

    def __init__(self):
        self._items: Dict[str, Item] = {}

    def add_item(self, name: str, quantity: int, unit_price: float) -> None:
        """Add or update an item in the inventory."""
        if name in self._items:
            self._items[name].quantity += quantity
        else:
            self._items[name] = Item(name, quantity, unit_price)

    def remove_item(self, name: str, quantity: int) -> None:
        """Remove a quantity of an item from the inventory."""
        if name in self._items:
            self._items[name].quantity = max(0, self._items[name].quantity - quantity)

    def total_inventory_value(self) -> float:
        """Return the total value of all items in inventory."""
        return sum(item.total_value() for item in self._items.values())


if __name__ == "__main__":
    inv = Inventory()
    inv.add_item("widget", 10, 2.5)
    inv.add_item("gadget", 5, 10.0)
    print(inv.total_inventory_value())
