# cafeteria/domain/order.py
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto

from .products import Product
from ..patterns.observer import Subject


class OrderStatus(Enum):
    PENDING = auto()
    PREPARING = auto()
    READY = auto()


@dataclass
class Order(Subject):
    """Concrete Subject that represents an order"""

    order_id: int
    customer_name: str
    product: Product
    status: OrderStatus = OrderStatus.PENDING

    def __post_init__(self) -> None:
        Subject.__init__(self)

    def change_status(self, new_status: OrderStatus) -> None:
        self.status = new_status
        if new_status == OrderStatus.READY:
            message = (
                f"Su pedido #{self.order_id} "
                f"({self.product.description()}) esta listo."
            )
            # This will call Customer.update, which is silent.
            self.notify(message)
