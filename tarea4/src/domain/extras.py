from __future__ import annotations
from abc import ABC
from .products import Product


class ExtraProductDecorator(Product, ABC):
    """
    Base decorator that wraps a Product and extends its description.

    It keeps the same kind() as the wrapped product (beverage or food),
    but modifies the Spanish description used in console output.
    """

    def __init__(self, base_product: Product) -> None:
        self._base_product = base_product

    def kind(self) -> str:
        return self._base_product.kind()


class WithMilk(ExtraProductDecorator):

    def description(self) -> str:
        return f"{self._base_product.description()} con leche"


class WithCinnamon(ExtraProductDecorator):

    def description(self) -> str:
        # This assumes the base description already includes previous extras
        return f"{self._base_product.description()} y canela"


class WithCream(ExtraProductDecorator):

    def description(self) -> str:
        return f"{self._base_product.description()} con crema"


class WithChocolateFilling(ExtraProductDecorator):

    def description(self) -> str:
        return f"{self._base_product.description()} con relleno de chocolate"
