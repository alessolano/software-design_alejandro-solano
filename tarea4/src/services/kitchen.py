from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain.order import Order


class Barista:
    """Service responsible for preparing beverages."""

    def prepare(self, order: "Order") -> None:
        product_text = order.product.description().capitalize()
        print(f"[Barista]: Preparo bebida: {product_text}")


class Baker:
    """Service responsible for preparing food items."""

    def prepare(self, order: "Order") -> None:
        product_text = order.product.description().capitalize()
        print(f"[Pastelero]: Preparo alimento: {product_text}")
