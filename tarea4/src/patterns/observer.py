from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, subject: "Subject", message: str) -> None:
        """Called by a Subject when it notifies its observers"""
        raise NotImplementedError


class Subject(ABC):
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Register a new observer if it is not already attached"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Remove an observer if it is currently attached"""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """Notify all attached observers with a given message"""
        for observer in self._observers:
            observer.update(self, message)
