from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def kind(self) -> str:
        """Return 'beverage' or 'food' to route preparation"""
        raise NotImplementedError


class Beverage(Product):
    def __init__(self, name: str) -> None:
        self._name = name

    def description(self) -> str:
        return self._name

    def kind(self) -> str:
        return "beverage"


class Food(Product):
    def __init__(self, name: str) -> None:
        self._name = name

    def description(self) -> str:
        return self._name

    def kind(self) -> str:
        return "food"
