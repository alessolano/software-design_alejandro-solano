from __future__ import annotations
from dataclasses import dataclass
from typing import List

from patterns.observer import Observer, Subject


@dataclass
class Customer(Observer):
    """Concrete observer that represents a customer"""

    name: str
    order_ids: List[int]

    def register_order(self, order_id: int) -> None:
        self.order_ids.append(order_id)

    def update(self, subject: Subject, message: str) -> None:
        """
        Unaltered to avoid output differences
        """
        return
