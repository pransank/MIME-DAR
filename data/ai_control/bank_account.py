"""
A simple bank account simulation with deposit and withdrawal logic.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Transaction:
    """Represents a single account transaction."""

    kind: str
    amount: float


@dataclass
class BankAccount:
    """A simple bank account."""

    owner: str
    balance: float = 0.0
    history: List[Transaction] = field(default_factory=list)

    def deposit(self, amount: float) -> None:
        """Deposit funds into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.history.append(Transaction("deposit", amount))

    def withdraw(self, amount: float) -> None:
        """Withdraw funds from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(Transaction("withdrawal", amount))


if __name__ == "__main__":
    account = BankAccount(owner="Jane Doe")
    account.deposit(100.0)
    account.withdraw(30.0)
    print(account.balance)
